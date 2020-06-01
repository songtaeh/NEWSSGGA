from django.shortcuts import render

# Create your views here.

def createpost(request):
    return render(request, 'createpost.html')