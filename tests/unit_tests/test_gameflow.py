from league_queuer.models.gameflow import Gameflow


def test_model_parsing() -> None:
    with open("tests/responses/lol-gameflow-v1-session.json") as json_file:
        gameflow = Gameflow.model_validate_json(json_file.read())
    assert gameflow.phase == "None"
