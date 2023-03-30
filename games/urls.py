from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("games", views.GameView)
router.register("categories", views.CategoryView)

urlpatterns = [
    path("", RedirectView.as_view(url="games"), name="root"),
    path("", include(router.urls)),
]
