import pytest

from games.models import Game
from tests.games.factories import GameFactory


@pytest.fixture(scope="class")
def game_factory() -> type[GameFactory]:
    """Return factory class."""
    return GameFactory


@pytest.fixture(scope="class")
def create_100_games(django_db_setup, django_db_blocker, game_factory) -> None:
    """Create 100 game objects in test database."""
    with django_db_blocker.unblock():
        Game.objects.all().delete()

        game_factory.create_batch(100)
