from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/<int:year>/<int:month>/<int:day>', views.shows, name='shows'),
    path('select/<int:show_id>', views.select, name='select'),
    path('reserve/<int:show_id>', views.reserve, name='reserve'),
]