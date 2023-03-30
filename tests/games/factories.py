import factory


class CategoryFactory(factory.django.DjangoModelFactory):
    """Generic category object factory."""

    class Meta:
        model = "games.Category"
        exclude = ("raw_title",)

    id = factory.Sequence(lambda n: n + 1)
    raw_title = factory.Faker("words", nb=1, unique=True)
    title = factory.LazyAttribute(lambda obj: obj.raw_title[0].title())
    url = factory.LazyAttribute(lambda obj: f"https://boardgamegeek.com/boardgame/{obj.id}/{obj.raw_title[0]}")
    description = factory.Faker("paragraph")


class GameFactory(factory.django.DjangoModelFactory):
    """Generic game object factory."""

    class Meta:
        model = "games.Game"
        exclude = ("raw_title", "slug_title")

    id = factory.Sequence(lambda n: n + 1)
    raw_title = factory.Faker("words", nb=3, unique=True)
    title = factory.LazyAttribute(lambda obj: " ".join(obj.raw_title).title())
    slug_title = factory.LazyAttribute(lambda obj: "-".join(obj.raw_title))
    year = factory.Iterator(range(2000, 2023))
    url = factory.LazyAttribute(lambda obj: f"https://boardgamegeek.com/boardgame/{obj.id}/{obj.slug_title}")
    description = factory.Faker("sentence")
