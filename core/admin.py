from django.contrib import admin
from cinema.models import Movie, Actor, Genre


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('actors',)


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
