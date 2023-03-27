import pytest

pytestmark = [pytest.mark.functional, pytest.mark.django_db]


class TestPaginatedGamesList:
    """As any user, I want to see a paginated games list when I open the page."""

    def test_root_redirects_to_games(self, api_client):
        """Root endpoint response redirects to games list endpoint."""
        response = api_client.get("/")

        assert response.status_code == 302
        assert response.url.strip("/") == "games"

    def test_response_items_attributes(self, api_client):
        """Game list contains objects with ID, title, year, URL, and description."""
        expected_attributes = {"id", "title", "year", "url", "description"}

        response = api_client.get("/games/")
        payload = response.json()

        assert response.status_code == 200
        assert isinstance(payload, list)
        for attribute in expected_attributes:
            assert attribute in payload[0].keys()

    def test_results_split_into_pages(self, api_client):
        """Games list is split into pages, which number is provided as page query argument."""
        response = api_client.get("/games/")
        response_2 = api_client.get("/games/?page=2")

        assert response_2.status_code == 200
        assert response.json() != response_2.json()

    def test_results_per_page_limit(self, api_client):
        """There are 20 games per page, and it's possible to change this limit by limit argument."""
        response = api_client.get("/games/")
        response_longer = api_client.get("/games/?limit=50")

        assert len(response.json()) == 20
        assert response_longer.status_code == 200
        assert len(response_longer.json()) == 50

    def test_results_total_count(self, api_client):
        """All objects count is available in X-Total-Count header."""
        response = api_client.get("/games/")

        assert response.headers.get("X-Total-Count") == "100"
