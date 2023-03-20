from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("games", views.GameView)

urlpatterns = [
    path("", views.RootView.as_view(), name="root_view"),
    path("", include(router.urls)),
]
