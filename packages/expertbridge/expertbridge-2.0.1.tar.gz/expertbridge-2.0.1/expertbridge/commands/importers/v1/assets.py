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
from typing import Any, Dict, List, Optional, Tuple

from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from expertbridge import db
from expertbridge.charts.commands.importers.v1.utils import import_chart
from expertbridge.charts.schemas import ImportV1ChartSchema
from expertbridge.commands.base import BaseCommand
from expertbridge.commands.exceptions import CommandInvalidError, ImportFailedError
from expertbridge.commands.importers.v1.utils import (
    load_configs,
    load_metadata,
    validate_metadata_type,
)
from expertbridge.dashboards.commands.importers.v1.utils import (
    find_chart_uuids,
    import_dashboard,
    update_id_refs,
)
from expertbridge.dashboards.schemas import ImportV1DashboardSchema
from expertbridge.databases.commands.importers.v1.utils import import_database
from expertbridge.databases.schemas import ImportV1DatabaseSchema
from expertbridge.datasets.commands.importers.v1.utils import import_dataset
from expertbridge.datasets.schemas import ImportV1DatasetSchema
from expertbridge.models.dashboard import dashboard_slices
from expertbridge.queries.saved_queries.commands.importers.v1.utils import (
    import_saved_query,
)
from expertbridge.queries.saved_queries.schemas import ImportV1SavedQuerySchema


class ImportAssetsCommand(BaseCommand):
    """
    Command for importing databases, datasets, charts, dashboards and saved queries.

    This command is used for managing Expertbridge assets externally under source control,
    and will overwrite everything.
    """

    schemas: Dict[str, Schema] = {
        "charts/": ImportV1ChartSchema(),
        "dashboards/": ImportV1DashboardSchema(),
        "datasets/": ImportV1DatasetSchema(),
        "databases/": ImportV1DatabaseSchema(),
        "queries/": ImportV1SavedQuerySchema(),
    }

    # pylint: disable=unused-argument
    def __init__(self, contents: Dict[str, str], *args: Any, **kwargs: Any):
        self.contents = contents
        self.passwords: Dict[str, str] = kwargs.get("passwords") or {}
        self._configs: Dict[str, Any] = {}

    # pylint: disable=too-many-locals
    @staticmethod
    def _import(session: Session, configs: Dict[str, Any]) -> None:
        # import databases first
        database_ids: Dict[str, int] = {}
        for file_name, config in configs.items():
            if file_name.startswith("databases/"):
                database = import_database(session, config, overwrite=True)
                database_ids[str(database.uuid)] = database.id

        # import saved queries
        for file_name, config in configs.items():
            if file_name.startswith("queries/"):
                config["db_id"] = database_ids[config["database_uuid"]]
                import_saved_query(session, config, overwrite=True)

        # import datasets
        dataset_info: Dict[str, Dict[str, Any]] = {}
        for file_name, config in configs.items():
            if file_name.startswith("datasets/"):
                config["database_id"] = database_ids[config["database_uuid"]]
                dataset = import_dataset(session, config, overwrite=True)
                dataset_info[str(dataset.uuid)] = {
                    "datasource_id": dataset.id,
                    "datasource_type": dataset.datasource_type,
                    "datasource_name": dataset.table_name,
                }

        # import charts
        chart_ids: Dict[str, int] = {}
        for file_name, config in configs.items():
            if file_name.startswith("charts/"):
                config.update(dataset_info[config["dataset_uuid"]])
                chart = import_chart(session, config, overwrite=True)
                chart_ids[str(chart.uuid)] = chart.id

        # store the existing relationship between dashboards and charts
        existing_relationships = session.execute(
            select([dashboard_slices.c.dashboard_id, dashboard_slices.c.slice_id])
        ).fetchall()

        # import dashboards
        dashboard_chart_ids: List[Tuple[int, int]] = []
        for file_name, config in configs.items():
            if file_name.startswith("dashboards/"):
                config = update_id_refs(config, chart_ids, dataset_info)
                dashboard = import_dashboard(session, config, overwrite=True)
                for uuid in find_chart_uuids(config["position"]):
                    if uuid not in chart_ids:
                        break
                    chart_id = chart_ids[uuid]
                    if (dashboard.id, chart_id) not in existing_relationships:
                        dashboard_chart_ids.append((dashboard.id, chart_id))

        # set ref in the dashboard_slices table
        values = [
            {"dashboard_id": dashboard_id, "slice_id": chart_id}
            for (dashboard_id, chart_id) in dashboard_chart_ids
        ]
        # pylint: disable=no-value-for-parameter # sqlalchemy/issues/4656
        session.execute(dashboard_slices.insert(), values)

    def run(self) -> None:
        self.validate()

        # rollback to prevent partial imports
        try:
            self._import(db.session, self._configs)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise ImportFailedError() from ex

    def validate(self) -> None:
        exceptions: List[ValidationError] = []

        # verify that the metadata file is present and valid
        try:
            metadata: Optional[Dict[str, str]] = load_metadata(self.contents)
        except ValidationError as exc:
            exceptions.append(exc)
            metadata = None
        validate_metadata_type(metadata, "assets", exceptions)

        self._configs = load_configs(
            self.contents, self.schemas, self.passwords, exceptions
        )

        if exceptions:
            exception = CommandInvalidError("Error importing assets")
            exception.add_list(exceptions)
            raise exception
