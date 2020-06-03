from django.shortcuts import render
from cafeapp.models import Cafe
from django.http import Http404
# Create your views here.

def mainpage(request):
    mycafe = Cafe.objects.all()
    return render(request, 'mainpage.html',{'mycafe':mycafe})
