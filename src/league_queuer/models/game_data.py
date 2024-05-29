from pydantic import BaseModel
from pydantic import Field

from league_queuer.models.player_champion_selection import PlayerChampionSelection
from league_queuer.models.queue import Queue
from league_queuer.models.team_one_item import TeamOneItem
from league_queuer.models.team_two_item import TeamTwoItem


class GameData(BaseModel):
    game_id: int = Field(..., alias="gameId")
    game_name: str = Field(..., alias="gameName")
    is_custom_game: bool = Field(..., alias="isCustomGame")
    password: str
    player_champion_selections: list[PlayerChampionSelection] = Field(..., alias="playerChampionSelections")
    queue: Queue
    spectators_allowed: bool = Field(..., alias="spectatorsAllowed")
    team_one: list[TeamOneItem] = Field(..., alias="teamOne")
    team_two: list[TeamTwoItem] = Field(..., alias="teamTwo")
