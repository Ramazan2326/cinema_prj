from django.test import TestCase, Client
from cinema import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.film = models.Movie.objects.create(
            title='Тачки',
            premiere='2006-07-20',
            description='Интересный анимационный фильм'
        )
        self.genre = models.Genre.objects.create(
            genre_title='Анимация'
        )

    def test_FilmsView(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_GenreView(self):
        response = self.client.get(self.genre.get_absolute_url())
        self.assertEqual(response.status_code, 200)
