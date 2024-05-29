from typing import Any

from pydantic import BaseModel
from pydantic import Field


class TeamOneItem(BaseModel):
    additional_prop1: dict[str, Any] = Field(..., alias="additionalProp1")
