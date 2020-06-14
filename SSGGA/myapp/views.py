from django.shortcuts import render
from cafeapp.models import Cafe
from django.http import Http404
from account.models import Profile
from django.contrib.auth.models import User
# Create your views here.
# 안녕

def mainpage(request):
    try:
        user = request.user
        p = user.profile

        mycafe = Cafe.objects.all()

        context = {'p':p, 'mycafe':mycafe}
        return render(request, 'mainpage.html', context)

    except:
        mycafe = Cafe.objects.all()

        context = {'mycafe':mycafe}
        return render(request, 'mainpage.html', context)
