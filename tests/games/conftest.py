import pytest

from games.models import Category, Game
from tests.games.factories import CategoryFactory, GameFactory


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


@pytest.fixture(scope="class")
def category_factory() -> type[CategoryFactory]:
    """Return factory class."""
    return CategoryFactory


@pytest.fixture(scope="class")
def create_categories(django_db_setup, django_db_blocker, category_factory) -> None:
    """Create 10 categories objects in test database."""
    with django_db_blocker.unblock():
        Category.objects.all().delete()

        category_factory.create_batch(10)
