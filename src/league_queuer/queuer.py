import time

from league_queuer.lcu_api import LcuApi


class Queueur:
    def __init__(self, lcu_api: LcuApi) -> None:
        self._lcu_api = lcu_api

    def run(self) -> None:
        while True:
            gameflow = self._lcu_api.gameflow()
            if gameflow.phase == "ReadyCheck":
                self._lcu_api.accept_queue()
            time.sleep(1)
