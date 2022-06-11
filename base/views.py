import datetime

from django.shortcuts import render

from .models import Movie

def index(request):
    today = datetime.date.today()
    return shows(request, today.year, today.month, today.day)

def shows(request, year, month, day):
    movies = Movie.objects.all()
    for movie in movies:
        movie.shows = movie.show_set.filter(date = datetime.date(year, month, day))
    movies = filter(lambda m: m.shows, movies)

    timeline = [datetime.date.today() + datetime.timedelta(n) for n in range(7)]

    ctx = {
        'movies': movies,
        'timeline': timeline
    }
    return render(request, 'base/shows.html', ctx)
