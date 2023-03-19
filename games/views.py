from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from . import models, serializers


class RootView(View):
    """Return JSON with alive confirmation."""

    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"status": "OK"})


class GamesView(View):
    """Return JSON with list of all Games."""

    def get(self, request: HttpRequest) -> JsonResponse:
        games = models.Game.objects.all()
        payload = [serializers.simple_model_serializer(game) for game in games]

        return JsonResponse(payload, safe=False)


class GameView(View):
    """Return JSON with Game by given ID."""

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        game = get_object_or_404(models.Game, id=pk)
        payload = serializers.simple_model_serializer(game)

        return JsonResponse(payload)
