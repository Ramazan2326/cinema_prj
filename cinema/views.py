from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cinema import models, serializers, filters
from .utils import *
from cinema import models
from cinema.forms import RegisterUserForm, LoginUserForm


def normalize_number(number):
    if number // 10 == 0:
        number = '0' + str(number)
    return number


def get_current_date_time():
    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    current_hour = current_date.hour
    current_minutes = current_date.minute

    current_day = normalize_number(current_day)
    current_month = normalize_number(current_month)
    current_hour = normalize_number(current_hour)
    current_minutes = normalize_number(current_minutes)
    dict_of_datetime = {
        "current_year": current_year,
        "current_day": current_day,
        "current_month": current_month,
        "current_hour": current_hour,
        "current_minutes": current_minutes
    }
    return dict_of_datetime


def login(request):
    return HttpResponseRedirect(reverse('home'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class FilmsView(TemplateView):
    model = models.Movie
    context_object_name = "film"
    template_name = 'core/index.html'

    def get_filters(self):
        return filters.Movie(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = {
            'films': self.get_queryset(),
            'genres': models.Genre.objects.all(),
            'title': 'Киноафиша',
            'datetime': get_current_date_time,
        }
        context['filters'] = self.get_filters()
        return context


class FilmsViewAPIView(APIView):
    def get(self, request):
        films_qs = models.Movie.objects.all()
        serializer = serializers.Movie(films_qs, many=True)
        titles = [film.title for film in films_qs]
        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Movie(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Фильм добавлен'})


class FilmsViewSet(ModelViewSet):
    queryset = models.Movie.objects.all()
    filterset_class = filters.Movie
    serializer_class = serializers.Movie


class GenreView(TemplateView):
    template_name = 'core/genre.html'

    def get_context_data(self, **kwargs):
        genre_id = kwargs['genre_id']
        films = models.Movie.objects.filter(genres=genre_id)
        genres = models.Genre.objects.all()
        count = models.Movie.objects.filter(genres=genre_id).count()
        datetime = get_current_date_time
        context = {
            'films': films,
            'genres': genres,
            'count': count,
            'datetime': datetime
        }
        return context


