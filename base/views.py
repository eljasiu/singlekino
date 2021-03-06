import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Movie, Show, Reservation
from .forms import UserForm

def loginView(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Taki użytkownik nie istnieje!')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Błędny email lub hasło!')

    ctx = {
        'page': page
    }
    return render(request, 'base/login_register.html', ctx)

def logoutView(request):
    logout(request)
    return redirect('index')

def registerView(request):
    page = 'register'
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.username = user.email.split('@')[0]
            user.save()
            return redirect('index')
        else:
            messages.error(request, 'Wystąpił błąd podczas rejestracji!')

    ctx = {
        'page': page,
        'form': form
    }
    return render(request, 'base/login_register.html', ctx)

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

@login_required(login_url='login')
def select(request, show_id):
    show = Show.objects.get(id=show_id)
    reserved = [str(reservation.row)+'-'+str(reservation.seat) for reservation in Reservation.objects.filter(show=show)]
    old = [str(reservation.row)+'-'+str(reservation.seat) for reservation in Reservation.objects.filter(user=request.user, show=show)]

    ctx = {
        'show': show,
        'reserved': reserved,
        'old': old
    }
    return render(request, 'base/select.html', ctx)

@login_required(login_url='login')
def reserve(request, show_id):
    show = Show.objects.get(id=show_id)
    user = request.user

    Reservation.objects.filter(user=user, show=show).delete()
    for place in request.POST.getlist('selected'):
        [row, seat] = place.split('-')
        reservation = Reservation(show=show, user=user, row=row, seat=seat)
        reservation.save()

    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')
def mine(request):
    reservations = Reservation.objects.filter(user=request.user)
    
    showDict = {}
    for reservation in reservations:
        if reservation.show in showDict:
            showDict[reservation.show].append(reservation)
        else:
            showDict[reservation.show] = [reservation]

    ctx = {
        'showDict': showDict
    }
    return render(request, 'base/mine.html', ctx)
