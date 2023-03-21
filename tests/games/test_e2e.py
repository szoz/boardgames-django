import pytest


@pytest.mark.django_db
class TestGetGames:
    def test_response(self, api_client):
        """All games endpoint returns list of games. Each game contains id, title, year, url and description."""
        expected_attributes = {"id", "title", "year", "url", "description"}

        response = api_client.get("/games/")
        payload = response.json()

        assert response.status_code == 200
        assert isinstance(payload, list)
        for game in payload:
            assert set(game.keys()) == expected_attributes

    def test_pages(self, api_client):
        """Games list is split into multiple pages. Endpoint returns 1st result page by default.
        If invalid page number is provided, endpoint will return not found error."""
        payload_default = api_client.get("/games/").json()

        response_1 = api_client.get("/games/?page=1")
        response_2 = api_client.get("/games/?page=2")
        response_not_found = api_client.get("/games/?page=1_000")

        assert response_1.status_code == 200
        assert response_2.status_code == 200
        assert response_1.json() == payload_default
        assert response_2.json() != payload_default
        assert response_not_found.status_code == 404

    def test_limit(self, api_client):
        """Games list contains 20 elements by default and supports different limits."""
        payload_default = api_client.get("/games/").json()
        payload_short = api_client.get("/games/?limit=10").json()
        payload_long = api_client.get("/games/?limit=50").json()

        assert len(payload_default) == 20
        assert len(payload_short) == 10
        assert len(payload_long) == 50

    def test_page_limit_combined(self, api_client):
        """Games list supports page and limit values in one query."""
        payload_all = api_client.get("/games/?limit=50").json()

        payload_1 = api_client.get("/games/?limit=25").json()
        payload_2 = api_client.get("/games/?limit=25&page=2").json()

        assert payload_1 + payload_2 == payload_all

    def test_pagination_headers(self, api_client):
        """Games list endpoint response contains header with total element count."""
        response_default = api_client.get("/games/")
        response_other = api_client.get("/games/?limit=25&page=2")

        assert response_default.headers["x-total-count"] == "100"
        assert response_other.headers["x-total-count"] == "100"


@pytest.mark.django_db
class TestGetGame:
    def test_found(self, api_client):
        """Game endpoint returns game object with given ID. This game object is the same as one returned in all
        games endpoint."""
        expected_game = api_client.get("/games/").json()[0]

        response = api_client.get(f'/games/{expected_game["id"]}/')
        payload = response.json()

        assert response.status_code == 200
        assert payload == expected_game

    def test_not_found(self, api_client):
        """Game endpoint returns not-found response when invalid game ID is provided."""
        response = api_client.get("/games/1_000_000/")

        assert response.status_code == 404
