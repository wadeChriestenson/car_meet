from django.urls import path
from salem import views

urlpatterns = [
    path('', views.carMeet, name='carMeet'),
]