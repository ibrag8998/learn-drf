from django.urls import path

from . import views as v

app_name = "snippets"
urlpatterns = [
    path("snippets/", v.snippet_list, name="list"),
    path("snippets/<int:pk>", v.snippet_detail, name="detail"),
]
