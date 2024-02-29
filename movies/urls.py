from django.urls import path

from .views import (
    index,
    MovieListView,
    ActorListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    MovieDetailView,
    ActorCreateView,
    ActorUpdateView,
    ActorDeleteView,
    ActorDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("movies/", MovieListView.as_view(), name="movies-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movies-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movies-create"),
    path("movies/<int:pk>/update/", MovieUpdateView.as_view(), name="movies-update"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movies-delete"),
    path("actors/", ActorListView.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actors-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actors-create"),
    path("actors/<int:pk>/update/", ActorUpdateView.as_view(), name="actors-update"),
    path("actors/<int:pk>/delete/", ActorDeleteView.as_view(), name="actors-delete"),
]

app_name = "movies"
