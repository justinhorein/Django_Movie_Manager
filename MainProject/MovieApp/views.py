from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie
from .api_connect import *
import requests


def home(request):
    return render(request, "MovieApp/movie_home.html")


def add_movie(request):
    form = MovieForm(request.POST or None)  # Gets the posted form if it exists
    if form.is_valid():  # Checks the form for errors
        form.save()  # Saves the movie to the database
        return redirect('listMovie')  # Redirects to home page
    else:
        print(form.errors)  # Prints any errors for the posted form to the terminal
        form = MovieForm()  # Creates a new blank form
    return render(request, 'MovieApp/movie_create.html', {'form': form})


def list_movie(request):
    get_movie = Movie.manager.all()
    context = {'movies': get_movie}
    return render(request, 'MovieApp/movie_index.html', context)


def movie_details(request, pk):
    pk = int(pk)
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie}
    return render(request, 'MovieApp/movie_details.html', context)


def edit_movie(request, pk):
    if request.method == "GET":
        pk = int(pk)
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, "MovieApp/movie_edit.html", {'form': form})

    else:
        if request.method == "POST":
            if 'submit' in request.POST:
                pk = int(pk)
                movie = get_object_or_404(Movie, pk=pk)
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                    form.save()
                return redirect('listMovie')
            else:
                pk = int(pk)
                movie = get_object_or_404(Movie, pk=pk)
                movie.delete()
                return redirect('listMovie')


def find_movie(request):
    context = {'movies': []}
    if request.method == 'POST':  # This block will handle all post backs from the forms
        title = request.POST["title"]
        year = request.POST["year"]
        mov_format = request.POST["mov_format"]
        results = get_search(year, mov_format, title)
        #print(results)
        if results["Response"] == "False":
            message = {'error': "You didn't enter any valid input"}
            context.update(message)
        else:
            for movies in results["Search"]:
                film = {'Title': movies['Title'],
                        'Year': movies['Year'],
                        'Format': movies['Type'],
                        'Poster': movies['Poster']
                }
                context['movies'].append(film)
    return render(request, 'MovieApp/movie_api.html', context)

