from django.shortcuts import render, redirect, get_object_or_404
from .forms import CafeForm
from .models import Cafe
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def createcafe(request):
    if request.method == "POST":
        cafeform = CafeForm(request.POST or None)
        print(cafeform.errors)
        if cafeform.is_valid():
            print(cafeform.errors)
            cafeform.save()
            return redirect('mainpage')
    cafeform = CafeForm()

    return render(request, 'createcafe.html',{'CafeForm':cafeform})

def searchcafe(request):
    br = Cafe.objects.all()
    b = request.GET.get('b','')
    if b:
        br = br.filter(title__icontains=b)

    return render(request,'searchcafe.html',{'searchcafe':br, 'b':b})