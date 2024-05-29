from pydantic import BaseModel


class AdditionalProp(BaseModel):
    spells: list[int]
