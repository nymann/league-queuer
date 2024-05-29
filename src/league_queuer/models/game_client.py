from pydantic import BaseModel
from pydantic import Field


class GameClient(BaseModel):
    observer_server_ip: str = Field(..., alias="observerServerIp")
    observer_server_port: int = Field(..., alias="observerServerPort")
    running: bool
    server_ip: str = Field(..., alias="serverIp")
    server_port: int = Field(..., alias="serverPort")
    visible: bool
