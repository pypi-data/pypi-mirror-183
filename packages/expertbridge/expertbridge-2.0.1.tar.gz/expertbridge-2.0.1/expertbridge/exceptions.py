# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from collections import defaultdict
from typing import Any, Dict, List, Optional

from flask_babel import gettext as _
from marshmallow import ValidationError

from expertbridge.errors import ErrorLevel, ExpertbridgeError, ExpertbridgeErrorType


class ExpertbridgeException(Exception):
    status = 500
    message = ""

    def __init__(
        self,
        message: str = "",
        exception: Optional[Exception] = None,
        error_type: Optional[ExpertbridgeErrorType] = None,
    ) -> None:
        if message:
            self.message = message
        self._exception = exception
        self._error_type = error_type
        super().__init__(self.message)

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    @property
    def error_type(self) -> Optional[ExpertbridgeErrorType]:
        return self._error_type

    def to_dict(self) -> Dict[str, Any]:
        rv = {}
        if hasattr(self, "message"):
            rv["message"] = self.message
        if self.error_type:
            rv["error_type"] = self.error_type
        if self.exception is not None and hasattr(self.exception, "to_dict"):
            rv = {**rv, **self.exception.to_dict()}  # type: ignore
        return rv


class ExpertbridgeErrorException(ExpertbridgeException):
    """Exceptions with a single ExpertbridgeErrorType associated with them"""

    def __init__(self, error: ExpertbridgeError, status: Optional[int] = None) -> None:
        super().__init__(error.message)
        self.error = error
        if status is not None:
            self.status = status

    def to_dict(self) -> Dict[str, Any]:
        return self.error.to_dict()


class ExpertbridgeGenericErrorException(ExpertbridgeErrorException):
    """Exceptions that are too generic to have their own type"""

    def __init__(self, message: str, status: Optional[int] = None) -> None:
        super().__init__(
            ExpertbridgeError(
                message=message,
                error_type=ExpertbridgeErrorType.GENERIC_BACKEND_ERROR,
                level=ErrorLevel.ERROR,
            )
        )
        if status is not None:
            self.status = status


class ExpertbridgeErrorFromParamsException(ExpertbridgeErrorException):
    """Exceptions that pass in parameters to construct a ExpertbridgeError"""

    def __init__(
        self,
        error_type: ExpertbridgeErrorType,
        message: str,
        level: ErrorLevel,
        extra: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            ExpertbridgeError(
                error_type=error_type, message=message, level=level, extra=extra or {}
            )
        )


class ExpertbridgeErrorsException(ExpertbridgeException):
    """Exceptions with multiple ExpertbridgeErrorType associated with them"""

    def __init__(
        self, errors: List[ExpertbridgeError], status: Optional[int] = None
    ) -> None:
        super().__init__(str(errors))
        self.errors = errors
        if status is not None:
            self.status = status


class ExpertbridgeTimeoutException(ExpertbridgeErrorFromParamsException):
    status = 408


class ExpertbridgeGenericDBErrorException(ExpertbridgeErrorFromParamsException):
    status = 400

    def __init__(
        self,
        message: str,
        level: ErrorLevel = ErrorLevel.ERROR,
        extra: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            ExpertbridgeErrorType.GENERIC_DB_ENGINE_ERROR,
            message,
            level,
            extra,
        )


class ExpertbridgeTemplateParamsErrorException(ExpertbridgeErrorFromParamsException):
    status = 400

    def __init__(
        self,
        message: str,
        error: ExpertbridgeErrorType,
        level: ErrorLevel = ErrorLevel.ERROR,
        extra: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            error,
            message,
            level,
            extra,
        )


class ExpertbridgeSecurityException(ExpertbridgeErrorException):
    status = 403

    def __init__(
        self, error: ExpertbridgeError, payload: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(error)
        self.payload = payload


class ExpertbridgeVizException(ExpertbridgeErrorsException):
    status = 400


class NoDataException(ExpertbridgeException):
    status = 400


class NullValueException(ExpertbridgeException):
    status = 400


class ExpertbridgeTemplateException(ExpertbridgeException):
    pass


class SpatialException(ExpertbridgeException):
    pass


class CertificateException(ExpertbridgeException):
    message = _("Invalid certificate")


class DatabaseNotFound(ExpertbridgeException):
    status = 400


class QueryObjectValidationError(ExpertbridgeException):
    status = 400


class AdvancedDataTypeResponseError(ExpertbridgeException):
    status = 400


class InvalidPostProcessingError(ExpertbridgeException):
    status = 400


class CacheLoadError(ExpertbridgeException):
    status = 404


class QueryClauseValidationException(ExpertbridgeException):
    status = 400


class DashboardImportException(ExpertbridgeException):
    pass


class DatasetInvalidPermissionEvaluationException(ExpertbridgeException):
    """
    When a dataset can't compute its permission name
    """


class SerializationError(ExpertbridgeException):
    pass


class InvalidPayloadFormatError(ExpertbridgeErrorException):
    status = 400

    def __init__(self, message: str = "Request payload has incorrect format"):
        error = ExpertbridgeError(
            message=message,
            error_type=ExpertbridgeErrorType.INVALID_PAYLOAD_FORMAT_ERROR,
            level=ErrorLevel.ERROR,
        )
        super().__init__(error)


class InvalidPayloadSchemaError(ExpertbridgeErrorException):
    status = 422

    def __init__(self, error: ValidationError):
        # dataclasses.asdict does not work with defaultdict, convert to dict
        # https://bugs.python.org/issue35540
        for k, v in error.messages.items():
            if isinstance(v, defaultdict):
                error.messages[k] = dict(v)
        error = ExpertbridgeError(
            message="An error happened when validating the request",
            error_type=ExpertbridgeErrorType.INVALID_PAYLOAD_SCHEMA_ERROR,
            level=ErrorLevel.ERROR,
            extra={"messages": error.messages},
        )
        super().__init__(error)


class ExpertbridgeCancelQueryException(ExpertbridgeException):
    status = 422
