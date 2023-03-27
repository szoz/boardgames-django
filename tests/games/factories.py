from faker import Faker

from games.models import Game

fake = Faker()


def game_factory(**kwargs) -> Game:
    """Create and return game object."""
    if kwargs.get("id"):
        fake.seed_instance(kwargs["id"])  # make test not-flaky

    title = fake.sentence(nb_words=3).rstrip(".")
    default = {
        "title": title,
        "year": 2023,
        "url": f'https://boardgamegeek.com/boardgame/{kwargs.get("id", 0)}/game',
        "description": f"{title} {fake.sentence().lower()}",
    }
    attributes = default | kwargs

    return Game(**attributes)
