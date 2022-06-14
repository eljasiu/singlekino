from django.contrib import admin

from .models import User, Movie, Show, Reservation

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Reservation)
