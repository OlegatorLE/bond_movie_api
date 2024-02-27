from django.urls import path

from .views import index, MovieListView, ActorListView

urlpatterns = [
    path("", index, name="index"),
    path("movies/", MovieListView.as_view(), name="movies-list"),
    path("actors/", ActorListView.as_view(), name="actors-list"),
]

app_name = "movies"
