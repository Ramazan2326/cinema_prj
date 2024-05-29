import django_filters
from cinema import models


class Movie(django_filters.FilterSet):
    title = django_filters.CharFilter(label='Название фильма',
                                      lookup_expr='icontains')
    class Meta:
        model = models.Movie
        exclude = ('poster', 'description', 'genres', 'premiere', 'actors',)
