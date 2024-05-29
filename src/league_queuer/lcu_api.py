import base64
import os

import requests

from league_queuer.models.gameflow import Gameflow


class LcuApi:
    def __init__(self, port: int, auth_token: str) -> None:
        self.port = port
        self.auth_token = auth_token
        self._headers = {"Authorization": f"Basic {auth_token}", "Accept": "application/json"}
        self._url = f"https://127.0.0.1:{port}"

    @classmethod
    def from_wmic(cls) -> "LcuApi":
        command = f"wmic process where \"caption='LeagueClientUx.exe'\" get Caption,Processid,Commandline"
        result = os.popen(command).read()
        port = int(result.split("app-port=")[2].split('"')[0])
        key = result.split("remoting-auth-token=")[1].split('"')[0]
        auth_token = base64.b64encode(f"riot:{key}".encode()).decode()
        return cls(port=port, auth_token=auth_token)

    def accept_queue(self) -> None:
        response = requests.post(f"{self._url}/lol-matchmaking/v1/ready-check/accept", headers=self._headers)
        response.raise_for_status()

    def gameflow(self) -> Gameflow:
        response = requests.get(f"{self._url}/lol-gameflow/v1/session", headers=self._headers)
        response.raise_for_status()
        return Gameflow.model_validate_json(response.json())
