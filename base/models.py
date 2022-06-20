import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.URLField()
    filmweb = models.URLField()

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['date', 'time']

    def is_past(self):
        return datetime.date.today() >= self.date and datetime.datetime.now().time() > self.time

    def __str__(self):
        return "{}_{}_{}".format(self.movie, self.date, self.time)

class Reservation(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.CharField(max_length=1)
    seat = models.IntegerField()

    def __str__(self):
        return "{}_{}_{}_{}".format(self.show, self.user, self.row, self.seat)
