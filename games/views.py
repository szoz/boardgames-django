from rest_framework import mixins, viewsets

from . import models, serializers


class GameView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Return JSON with game by given ID or list of all games."""

    queryset = models.Game.objects.order_by("id").all()
    serializer_class = serializers.GameSerializer
