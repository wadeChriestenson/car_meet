from django.shortcuts import render


# Create your views here.
def carMeet(request):
    return render(request, 'car_meets.html', {})
