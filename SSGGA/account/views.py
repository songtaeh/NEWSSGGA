from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect('index')
        else:
            return redirect('register')
    registerform = UserCreationForm
    return render(request, 'registration/register.html', {'registerform':registerform})
