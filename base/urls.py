from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/<int:year>/<int:month>/<int:day>', views.shows, name='shows'),
]