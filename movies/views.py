from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .filters import MovieFilter
from django_filters.views import FilterView
from movies.models import Movie, Actor


def index(request):
    """View function for the home page of the site."""

    num_movies = Movie.objects.count()
    num_actors = Actor.objects.count()
    print(num_actors, num_movies)

    context = {
        "num_movies": num_movies,
        "num_actors": num_actors,
    }

    return render(request, "movies/index.html", context=context)


class MovieListView(FilterView):
    model = Movie
    queryset = Movie.objects.order_by('id')
    filterset_class = MovieFilter
    template_name = "movies/movie_list.html"
    paginate_by = 25


class MovieCreateView(generic.CreateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("movies:movies-list")


class MovieUpdateView(generic.UpdateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("movies:movies-list")


class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = reverse_lazy("movies:movies-list")


class ActorListView(generic.ListView):
    model = Actor
    queryset = Actor.objects.order_by("id")
    paginate_by = 25
