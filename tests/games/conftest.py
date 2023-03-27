import pytest

from games.models import Game
from tests.games.factories import game_factory


@pytest.fixture(scope="class")
def create_games(django_db_setup, django_db_blocker) -> None:
    """Create 100 game objects in test database."""
    with django_db_blocker.unblock():
        Game.objects.all().delete()

        for count in range(100):
            game = game_factory(id=count + 1)
            game.save()
