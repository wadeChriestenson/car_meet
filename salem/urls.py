from django.urls import path
from salem import views

urlpatterns = [
    path('', views.carMeet, name='carMeet'),
    path('setup.html', views.setup, name='setup'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('disclaimer.html', views.disclaimer, name='disclaimer')
]