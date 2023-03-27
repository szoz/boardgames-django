import pytest
from django.db.utils import IntegrityError

from tests.games.factories import game_factory

pytestmark = [pytest.mark.unit, pytest.mark.django_db]


class TestGame:
    def test_create(self):
        """Game object can be created."""
        game = game_factory()

        game.save()

    @pytest.mark.xfail  # TODO switch to postgres and remove this mark
    @pytest.mark.parametrize(
        "attribute,value", [("title", 105 * "x"), ("url", "https://boardgamegeek.com/" + 80 * "x")]
    )
    def test_too_long_fields(self, attribute: str, value: str):
        """Game object can't have too long title or url values."""
        game = game_factory(**{attribute: value})

        with pytest.raises(IntegrityError):
            game.save()

    @pytest.mark.parametrize("attribute,value", [("title", "A game"), ("url", "https://boardgamegeek.com/x")])
    def test_unique_fields(self, attribute: str, value: str):
        """Category object must have unique title and url values."""
        game_factory(title="A game").save()

        with pytest.raises(IntegrityError):
            game_factory(title="A game").save()
