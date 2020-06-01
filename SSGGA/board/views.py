from django.shortcuts import render
from .models import Board
from .forms import BoardForm

# Create your views here.

def createpost(request):
    all_post = Board.objects.all()

    context = {'take_all_post':all_post}
    return render(request, 'createpost.html', context)