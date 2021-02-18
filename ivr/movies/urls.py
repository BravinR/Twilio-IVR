# movies/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('answer', views.answer, name='choose-theater'),
    path('choose-movie', views.choose_movie, name='choose-movie'),
    path('list-showtimes', views.list_showtimes, name='list-showtimes'),
]