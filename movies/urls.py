from django.urls import path

from .views import index, MovieListView

urlpatterns = [
    path("", index, name="index"),
    path("movies/", MovieListView.as_view(), name="movies-list"),
]

app_name = "movies"
