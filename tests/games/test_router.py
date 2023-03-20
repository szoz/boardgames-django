import pytest


@pytest.mark.django_db
class TestGetGames:
    def test_get_games_response(self, api_client):
        """All games endpoint returns list of games. Each game contains id, title, year, url and description."""
        expected_attributes = {"id", "title", "year", "url", "description"}

        response = api_client.get("/games/")
        payload = response.json()

        assert response.status_code == 200
        assert isinstance(payload, list)
        for game in payload:
            assert set(game.keys()) == expected_attributes


@pytest.mark.django_db
class TestGetGame:
    def test_game_found(self, api_client):
        """Game endpoint returns game object with given ID. This game object is the same as one returned in all
        games endpoint."""
        expected_game = api_client.get("/games/").json()[0]

        response = api_client.get(f'/games/{expected_game["id"]}/')
        payload = response.json()

        assert response.status_code == 200
        assert payload == expected_game

    def test_game_not_found(self, api_client):
        """Game endpoint returns not-found response when invalid game ID is provided."""
        games_max_id = max(game["id"] for game in api_client.get("/games/").json())

        response = api_client.get(f"/games/{games_max_id + 1}/")

        assert response.status_code == 404
