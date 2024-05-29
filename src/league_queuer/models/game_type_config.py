from pydantic import BaseModel
from pydantic import Field


class GameTypeConfig(BaseModel):
    advanced_learning_quests: bool = Field(..., alias="advancedLearningQuests")
    allow_trades: bool = Field(..., alias="allowTrades")
    ban_mode: str = Field(..., alias="banMode")
    ban_timer_duration: int = Field(..., alias="banTimerDuration")
    battle_boost: bool = Field(..., alias="battleBoost")
    cross_team_champion_pool: bool = Field(..., alias="crossTeamChampionPool")
    death_match: bool = Field(..., alias="deathMatch")
    do_not_remove: bool = Field(..., alias="doNotRemove")
    duplicate_pick: bool = Field(..., alias="duplicatePick")
    exclusive_pick: bool = Field(..., alias="exclusivePick")
    id: int
    learning_quests: bool = Field(..., alias="learningQuests")
    main_pick_timer_duration: int = Field(..., alias="mainPickTimerDuration")
    max_allowable_bans: int = Field(..., alias="maxAllowableBans")
    name: str
    onboard_coop_beginner: bool = Field(..., alias="onboardCoopBeginner")
    pick_mode: str = Field(..., alias="pickMode")
    post_pick_timer_duration: int = Field(..., alias="postPickTimerDuration")
    reroll: bool
    team_champion_pool: bool = Field(..., alias="teamChampionPool")
