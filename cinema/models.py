from django.db import models


class Movie(models.Model):
    title = models.CharField('Название', max_length=20, blank=False, unique=True)
    premiere = models.DateField('Дата премьеры')
    description = models.TextField('Описание фильма', max_length=500, blank=True)
    poster = models.ImageField('Постер', upload_to='posters', blank=True)
    actors = models.ManyToManyField('Actor', verbose_name='Актер', blank=True)
    genres = models.ManyToManyField('Genre', verbose_name='Жанр', blank=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.title


class Genre(models.Model):
    CHOICES = (
        ('fantasy', 'Фэнтези'),
        ('adventures', 'Приключения'),
        ('action', 'Боевик'),
        ('drama', 'Драма'),
        ('thriller', 'Триллер'),
        ('comedy', 'Комедия'),
    )
    genre_title = models.CharField('Жанр', choices=CHOICES, max_length=20,
                                   blank=True)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def get_absolute_url(self):
        return f"/genres/{self.pk}/"

    def __str__(self):
        return self.genre_title


class Actor(models.Model):
    first_name = models.CharField('Имя', max_length=20, blank=False)
    last_name = models.CharField('Фамилия', max_length=20, blank=False)
    nickname = models.CharField('Прозвище', max_length=20, blank=True)
    salary = models.DecimalField('Зарплата', max_digits=5, decimal_places=2,
                                 blank=True)
    profile_image = models.ImageField('Фото', upload_to='profile_images',
                                      blank=True)
    has_oscar = models.BooleanField('Лауреат Оскара', default=False,
                                    blank=False)

    class Meta:
        verbose_name = 'актер'
        verbose_name_plural = 'актеры'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
