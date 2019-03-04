from django.shortcuts import render
from django.http import HttpResponse
from .forms import fitnessForm
from .models import foodInfo
from django.contrib.auth.models import User


# Create your views here.



# view function for index page


def index(request):
    return render(request, 'foodFitnessApp/index.html')


# view function for creating a new account

def newAppUser(request):
    form = fitnessForm(request.POST or None)
    context = {"form": form}
    return render(request, 'foodFitnessApp/newUser.html', context)


# view funtion for saving info in the form above

def saveNewUser(request):
    form = fitnessForm(request.POST or None)
    if request.method == "POST":
        User.objects.create_user(request.POST['username'])
        form.save()
        return render(request, 'foodFitnessApp/welcome.html')