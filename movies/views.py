from django.shortcuts import render
from django.views import generic

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


class MovieListView(generic.ListView):
    model = Movie
    queryset = Movie.objects.order_by('id')
    paginate_by = 25
