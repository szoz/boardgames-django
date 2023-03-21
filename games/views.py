from django.http import HttpRequest, JsonResponse
from django.views import View
from rest_framework import mixins, viewsets

from . import models, serializers


class RootView(View):
    """Return JSON with alive confirmation."""

    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"status": "OK"})


class GameView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Return JSON with game by given ID or list of all games."""

    queryset = models.Game.objects.order_by("id").all()
    serializer_class = serializers.GameSerializer
