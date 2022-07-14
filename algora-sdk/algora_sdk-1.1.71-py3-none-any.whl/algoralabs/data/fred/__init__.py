from typing import Optional

from pydantic import Field, validator

from algoralabs.common.base import Base
from algoralabs.common.types import Datetime


class FredQuery(Base):
    api_key: str
    series_id: str
    file_type: str = Field(default='json')
    observation_start: Optional[Datetime] = None
    observation_end: Optional[Datetime] = None

    # necessary for proper .dict() serialization
    @validator("observation_start")
    def observation_start_to_string(cls, d):
        return d.isoformat()

    @validator("observation_end")
    def observation_end_to_string(cls, d):
        return d.isoformat()
