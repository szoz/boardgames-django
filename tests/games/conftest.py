import pytest

from games.models import Game


@pytest.fixture(scope="session", autouse=True)
def create_games(django_db_setup, django_db_blocker):
    """Create 100 game objects in test database."""
    with django_db_blocker.unblock():
        current_games = Game.objects.all()
        current_games.delete()

        for count in range(1, 101):
            serialized_game = {
                "id": count,
                "title": f"Game {count}",
                "year": 2023,
                "url": f"https://boardgamegeek.com/boardgame/{count}/game",
                "description": f"Game {count} description",
            }
            game = Game(**serialized_game)
            game.save()
