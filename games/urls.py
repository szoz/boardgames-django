from django.urls import path

from games.views import GamesView, GameView, RootView

urlpatterns = [
    path("", RootView.as_view(), name="root_view"),
    path("games", GamesView.as_view(), name="game_list"),
    path("games/<int:pk>", GameView.as_view(), name="game_list"),
]
