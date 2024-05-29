from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema import views
from django.conf.urls.static import static
from core import settings
import cinema.views

router = DefaultRouter()
router.register('filmsviewset', views.FilmsViewSet, basename='filmsviewset')


urlpatterns = [
    path('home/', cinema.views.FilmsView.as_view(), name="home"),
    path('genres/<int:genre_id>/', cinema.views.GenreView.as_view()),
    path('films/', cinema.views.FilmsViewAPIView.as_view()),
    path('', cinema.views.RegisterUser.as_view(), name="registration"),
    path('login/', cinema.views.LoginUser.as_view(), name="login"),
    path('logout/', cinema.views.user_logout, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls