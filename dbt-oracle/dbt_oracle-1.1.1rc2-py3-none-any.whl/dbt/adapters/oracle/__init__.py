"""
Copyright (c) 2022, Oracle and/or its affiliates.
Copyright (c) 2020, Vitor Avancini

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""
from dbt.adapters.oracle.connections import OracleAdapterConnectionManager
from dbt.adapters.oracle.connections import OracleAdapterCredentials
from dbt.adapters.oracle.impl import OracleAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import oracle

Plugin = AdapterPlugin(
    adapter=OracleAdapter,
    credentials=OracleAdapterCredentials,
    include_path=oracle.PACKAGE_PATH
)
