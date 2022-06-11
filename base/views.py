import datetime

from django.shortcuts import render

from .models import Movie, Show, Reservation

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

def reserve(request, show_id):
    show = Show.objects.get(id=show_id)

    reserved = [str(reservation.row)+'-'+str(reservation.seat) for reservation in Reservation.objects.filter(show = show)]

    ctx = {
        'show': show,
        'reserved': reserved
        }
    return render(request, 'base/reserve.html', ctx)
