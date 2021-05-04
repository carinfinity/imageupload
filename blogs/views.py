from django.shortcuts import render
from .forms import newCarBlogs
from .models import NewCar

# Create your views here.

def newCar(request):
    fg = NewCar.objects.all()
    print(fg)
    return render(request, 'blogs/newcar.html', {'car': fg})


def upcomingCar(request):
    return render(request, 'blogs/upcomingcar.html')