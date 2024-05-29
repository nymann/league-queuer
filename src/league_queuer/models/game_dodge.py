from pydantic import BaseModel
from pydantic import Field


class GameDodge(BaseModel):
    dodge_ids: list[int] = Field(..., alias="dodgeIds")
    phase: str
    state: str
