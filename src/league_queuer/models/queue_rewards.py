from pydantic import BaseModel
from pydantic import Field


class QueueRewards(BaseModel):
    is_champion_points_enabled: bool = Field(..., alias="isChampionPointsEnabled")
    is_ip_enabled: bool = Field(..., alias="isIpEnabled")
    is_xp_enabled: bool = Field(..., alias="isXpEnabled")
    party_size_ip_rewards: list[int] = Field(..., alias="partySizeIpRewards")
