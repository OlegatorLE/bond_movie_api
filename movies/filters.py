import django_filters

from .models import Movie


class MovieFilter(django_filters.FilterSet):
    release_year = django_filters.CharFilter(field_name="release_year", lookup_expr='exact', label="Year")
    director = django_filters.CharFilter(field_name="director", lookup_expr='icontains', label="Director")
    actors__name = django_filters.CharFilter(field_name="actors__name", lookup_expr='icontains', label="Actor")


    class Meta:
        model = Movie
        fields = ["release_year", "director", "actors__name"]
