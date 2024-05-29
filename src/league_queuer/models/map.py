from pydantic import BaseModel
from pydantic import Field

from league_queuer.models.asssets import Assets
from league_queuer.models.categorized_content_bundles import CategorizedContentBundles
from league_queuer.models.per_position_disallowed_summoner_spells import PerPositionDisallowedSummonerSpells
from league_queuer.models.per_position_required_summoner_spells import PerPositionRequiredSummonerSpells
from league_queuer.models.properties import Properties


class Map(BaseModel):
    assets: Assets
    categorized_content_bundles: CategorizedContentBundles = Field(..., alias="categorizedContentBundles")
    description: str
    game_mode: str = Field(..., alias="gameMode")
    game_mode_name: str = Field(..., alias="gameModeName")
    game_mode_short_name: str = Field(..., alias="gameModeShortName")
    game_mutator: str = Field(..., alias="gameMutator")
    id: int
    is_rgm: bool = Field(..., alias="isRGM")
    map_string_id: str = Field(..., alias="mapStringId")
    name: str
    per_position_disallowed_summoner_spells: PerPositionDisallowedSummonerSpells = Field(
        ...,
        alias="perPositionDisallowedSummonerSpells",
    )
    per_position_required_summoner_spells: PerPositionRequiredSummonerSpells = Field(
        ...,
        alias="perPositionRequiredSummonerSpells",
    )
    platform_id: str = Field(..., alias="platformId")
    platform_name: str = Field(..., alias="platformName")
    properties: Properties
