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
    queryset = Movie.objects.order_by("id")
    filterset_class = MovieFilter
    template_name = "movies/movie_list.html"
    paginate_by = 25


class MovieDetailView(generic.DetailView):
    model = Movie


class MovieCreateView(generic.CreateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("movies:movies-list")


class MovieUpdateView(generic.UpdateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("movies:movies-detail", kwargs={"pk": self.object.pk})


class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = reverse_lazy("movies:movies-list")


class ActorListView(generic.ListView):
    model = Actor
    queryset = Actor.objects.order_by("id")
    paginate_by = 25


class ActorDetailView(generic.DetailView):
    model = Actor


class ActorCreateView(generic.CreateView):
    model = Actor
    fields = "__all__"
    success_url = reverse_lazy("movies:actors-list")


class ActorUpdateView(generic.UpdateView):
    model = Actor
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("movies:actors-detail", kwargs={"pk": self.object.pk})


class ActorDeleteView(generic.DeleteView):
    model = Actor
    success_url = reverse_lazy("movies:actors-list")
