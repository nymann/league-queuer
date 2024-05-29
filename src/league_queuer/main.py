import typer

from league_queuer.lcu_api import LcuApi
from league_queuer.queuer import Queueur

app = typer.Typer()


@app.command()
def main() -> None:
    lcu_api = LcuApi.from_wmic()
    queuer = Queueur(lcu_api=lcu_api)
    queuer.run()


if __name__ == "__main__":
    app()
