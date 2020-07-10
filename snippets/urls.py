from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as v

r = DefaultRouter()
r.register("snippets", v.SnippetViewSet)
r.register("users", v.UserViewSet)

urlpatterns = [
    path("", include(r.urls)),
]
