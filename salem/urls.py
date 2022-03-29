from django.urls import path
from salem import views

urlpatterns = [
    path('', views.carMeet, name='carMeet'),
    path('setupameet.html', views.setup, name='setupameet')
]