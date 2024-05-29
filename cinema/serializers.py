from rest_framework import serializers
from cinema import models


class Movie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class Genre(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'
