import pytest
from django.db.utils import IntegrityError

from tests.games.factories import CategoryFactory, GameFactory

pytestmark = [pytest.mark.unit, pytest.mark.django_db]


class TestGame:
    def test_create(self, game_factory: GameFactory):
        """Game object can be created. It contains id, title, year, url and description attributes."""
        expected_attributes_types = {"id": int, "title": str, "year": int, "url": str, "description": str}

        game = game_factory.build()
        game.save()

        for attribute, type_ in expected_attributes_types.items():
            assert isinstance(getattr(game, attribute), type_)

    @pytest.mark.xfail  # TODO switch to postgres and remove this mark
    @pytest.mark.parametrize(
        "attribute,value", [("title", 105 * "x"), ("url", "https://boardgamegeek.com/" + 80 * "x")]
    )
    def test_too_long_fields(self, game_factory: GameFactory, attribute: str, value: str):
        """Game object can't have too long title or url values."""
        game = game_factory.build(**{attribute: value})

        with pytest.raises(IntegrityError):
            game.save()

    @pytest.mark.parametrize("attribute,value", [("title", "A game"), ("url", "https://boardgamegeek.com/x")])
    def test_unique_fields(self, game_factory: GameFactory, attribute: str, value: str):
        """Category object must have unique title and url values."""
        game_factory.build(title="A game").save()

        with pytest.raises(IntegrityError):
            game_factory.build(title="A game").save()


class TestCategory:
    def test_create(self, category_factory: CategoryFactory):
        """Category object can be created. It contains id, title, url and description attributes."""
        expected_attributes_types = {"id": int, "title": str, "url": str, "description": str}

        category = category_factory.build()
        category.save()

        for attribute, type_ in expected_attributes_types.items():
            assert isinstance(getattr(category, attribute), type_)

    @pytest.mark.xfail  # TODO switch to postgres and remove this mark
    @pytest.mark.parametrize(
        "attribute,value", [("title", 105 * "x"), ("url", "https://boardgamegeek.com/" + 80 * "x")]
    )
    def test_too_long_fields(self, category_factory: CategoryFactory, attribute: str, value: str):
        """Game object can't have too long title or url values."""
        game = category_factory.build(**{attribute: value})

        with pytest.raises(IntegrityError):
            game.save()

    @pytest.mark.parametrize("attribute,value", [("title", "A category"), ("url", "https://boardgamegeek.com/x")])
    def test_unique_fields(self, category_factory: CategoryFactory, attribute: str, value: str):
        """Category object must have unique title and url values."""
        category_factory.build(title="A game").save()

        with pytest.raises(IntegrityError):
            category_factory.build(title="A game").save()
