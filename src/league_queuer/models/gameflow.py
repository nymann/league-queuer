from pydantic import BaseModel
from pydantic import Field

from league_queuer.models.game_client import GameClient
from league_queuer.models.game_data import GameData
from league_queuer.models.game_dodge import GameDodge
from league_queuer.models.map import Map


class Gameflow(BaseModel):
    game_client: GameClient = Field(..., alias="gameClient")
    game_data: GameData = Field(..., alias="gameData")
    game_dodge: GameDodge = Field(..., alias="gameDodge")
    map: Map
    phase: str
