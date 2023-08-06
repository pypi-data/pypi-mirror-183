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
from flask import session

from expertbridge.dashboards.filter_state.commands.utils import check_access
from expertbridge.extensions import cache_manager
from expertbridge.key_value.utils import get_owner
from expertbridge.temporary_cache.commands.delete import DeleteTemporaryCacheCommand
from expertbridge.temporary_cache.commands.entry import Entry
from expertbridge.temporary_cache.commands.exceptions import TemporaryCacheAccessDeniedError
from expertbridge.temporary_cache.commands.parameters import CommandParameters
from expertbridge.temporary_cache.utils import cache_key


class DeleteFilterStateCommand(DeleteTemporaryCacheCommand):
    def delete(self, cmd_params: CommandParameters) -> bool:
        resource_id = cmd_params.resource_id
        actor = cmd_params.actor
        key = cache_key(resource_id, cmd_params.key)
        check_access(resource_id)
        entry: Entry = cache_manager.filter_state_cache.get(key)
        if entry:
            if entry["owner"] != get_owner(actor):
                raise TemporaryCacheAccessDeniedError()
            tab_id = cmd_params.tab_id
            contextual_key = cache_key(session.get("_id"), tab_id, resource_id)
            cache_manager.filter_state_cache.delete(contextual_key)
            return cache_manager.filter_state_cache.delete(key)
        return False
