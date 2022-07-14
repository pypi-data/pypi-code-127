#
# Copyright 2022 aiohomekit team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Mechanism to cache characteristic database.

It is slow to query the BLE characteristics to find their iid and
signatures. We only need to do this work when the cn has incremented.

This interface must be kept compatible with Home Assistant. This is a
dumb implementation for development and CLI usage.
"""

from __future__ import annotations

import json
import logging
import pathlib
from typing import Any, Protocol, TypedDict

logger = logging.getLogger(__name__)


class Pairing(TypedDict):
    """A versioned map of entity metadata as presented by aiohomekit."""

    config_num: int
    accessories: list[Any]


class StorageLayout(TypedDict):
    """Cached pairing metadata needed by aiohomekit."""

    pairings: dict[str, Pairing]


class CharacteristicCacheType(Protocol):
    def get_map(self, homekit_id: str) -> Pairing | None:
        pass

    def async_create_or_update_map(
        self, homekit_id: str, config_num: int, accessories: list[Any]
    ) -> Pairing:
        pass

    def async_delete_map(self, homekit_id: str) -> None:
        pass


class CharacteristicCacheMemory:
    def __init__(self) -> None:
        """Create a new entity map store."""
        self.storage_data: dict[str, Pairing] = {}

    def get_map(self, homekit_id: str) -> Pairing | None:
        """Get a pairing cache item."""
        return self.storage_data.get(homekit_id)

    def async_create_or_update_map(
        self, homekit_id: str, config_num: int, accessories: list[Any]
    ) -> Pairing:
        """Create a new pairing cache."""
        data = Pairing(config_num=config_num, accessories=accessories)
        self.storage_data[homekit_id] = data
        return data

    def async_delete_map(self, homekit_id: str) -> None:
        """Delete pairing cache."""
        if homekit_id not in self.storage_data:
            return

        self.storage_data.pop(homekit_id)


class CharacteristicCacheFile(CharacteristicCacheMemory):
    def __init__(self, location: pathlib.Path) -> None:
        """Create a new entity map store."""
        super().__init__()

        self.location = location
        if location.exists():
            with open(location) as fp:
                try:
                    self.storage_data = json.load(fp)["pairings"]
                except json.decoder.JSONDecodeError:
                    logger.debug(
                        "Characteristic cache was corrupted, proceeding with cold cache"
                    )

    def async_create_or_update_map(
        self, homekit_id: str, config_num: int, accessories: list[Any]
    ) -> Pairing:
        """Create a new pairing cache."""
        data = super().async_create_or_update_map(homekit_id, config_num, accessories)
        self._do_save()
        return data

    def async_delete_map(self, homekit_id: str) -> None:
        """Delete pairing cache."""
        super().async_delete_map(homekit_id)
        self._do_save()

    def _do_save(self) -> None:
        """Schedule saving the entity map cache."""
        with open(self.location, "w") as fp:
            fp.write(json.dumps(self._data_to_save()))

    def _data_to_save(self) -> dict[str, Any]:
        """Return data of entity map to store in a file."""
        return StorageLayout(pairings=self.storage_data)
