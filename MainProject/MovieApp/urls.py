from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name="movieHome"),
    path('AddToCollection/', views.add_movie, name='createMovie'),  # add a movie title
    path('YourMovies/', views.list_movie, name='listMovie'),
    path('YourMovies/<int:pk>/Details/', views.movie_details, name='movieDetails'),
    path('YourMovies/<int:pk>/Edit/', views.edit_movie, name='editMovie'),
    path ('FindMovies', views.find_movie, name='findMovie'),
]