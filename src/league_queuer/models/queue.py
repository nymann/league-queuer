from pydantic import BaseModel
from pydantic import Field

from league_queuer.models.game_type_config import GameTypeConfig
from league_queuer.models.queue_rewards import QueueRewards


class Queue(BaseModel):
    allowable_premade_sizes: list[int] = Field(..., alias="allowablePremadeSizes")
    are_free_champions_allowed: bool = Field(..., alias="areFreeChampionsAllowed")
    asset_mutator: str = Field(..., alias="assetMutator")
    category: str
    champions_required_to_play: int = Field(..., alias="championsRequiredToPlay")
    description: str
    detailed_description: str = Field(..., alias="detailedDescription")
    game_mode: str = Field(..., alias="gameMode")
    game_type_config: GameTypeConfig = Field(..., alias="gameTypeConfig")
    id: int
    is_ranked: bool = Field(..., alias="isRanked")
    is_team_builder_managed: bool = Field(..., alias="isTeamBuilderManaged")
    is_team_only: bool = Field(..., alias="isTeamOnly")
    last_toggled_off_time: int = Field(..., alias="lastToggledOffTime")
    last_toggled_on_time: int = Field(..., alias="lastToggledOnTime")
    map_id: int = Field(..., alias="mapId")
    max_level: int = Field(..., alias="maxLevel")
    max_summoner_level_for_first_win_of_the_day: int = Field(..., alias="maxSummonerLevelForFirstWinOfTheDay")
    maximum_participant_list_size: int = Field(..., alias="maximumParticipantListSize")
    min_level: int = Field(..., alias="minLevel")
    minimum_participant_list_size: int = Field(..., alias="minimumParticipantListSize")
    name: str
    num_players_per_team: int = Field(..., alias="numPlayersPerTeam")
    queue_availability: str = Field(..., alias="queueAvailability")
    queue_rewards: QueueRewards = Field(..., alias="queueRewards")
    removal_from_game_allowed: bool = Field(..., alias="removalFromGameAllowed")
    removal_from_game_delay_minutes: int = Field(..., alias="removalFromGameDelayMinutes")
    short_name: str = Field(..., alias="shortName")
    show_position_selector: bool = Field(..., alias="showPositionSelector")
    spectator_enabled: bool = Field(..., alias="spectatorEnabled")
    type: str
