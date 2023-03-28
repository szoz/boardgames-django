import factory


class GameFactory(factory.django.DjangoModelFactory):
    """Generic game object factory."""

    class Meta:
        model = "games.Game"

    id = factory.Sequence(lambda n: n + 1)
    title = factory.Sequence(lambda n: f"Game {n}")
    year = factory.Iterator(range(2000, 2023))
    url = factory.LazyAttribute(lambda obj: f"https://boardgamegeek.com/boardgame/{obj.id}/game")
    description = factory.Faker("sentence")
