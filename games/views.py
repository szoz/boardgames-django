from rest_framework import mixins, viewsets

from .models import Category, Game
from .serializers import CategorySerializer, GameSerializer
from .utils import SimplePagePagination


class GameView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Return JSON with games list or game by given ID."""

    queryset = Game.objects.order_by("id").all()
    serializer_class = GameSerializer
    pagination_class = SimplePagePagination


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Return JSON with categories list or category by given ID."""

    queryset = Category.objects.order_by("id").all()
    serializer_class = CategorySerializer
