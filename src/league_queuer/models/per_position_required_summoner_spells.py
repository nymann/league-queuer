from pydantic import BaseModel
from pydantic import Field

from league_queuer.models.additional_prop import AdditionalProp


class PerPositionRequiredSummonerSpells(BaseModel):
    additional_prop1: AdditionalProp = Field(..., alias="additionalProp1")
    additional_prop2: AdditionalProp = Field(..., alias="additionalProp2")
    additional_prop3: AdditionalProp = Field(..., alias="additionalProp3")
