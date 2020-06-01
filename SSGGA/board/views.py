from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm

# Create your views here.

def createpost(request):
    if request.method == "POST":
        myform = BoardForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('board')
    myform = BoardForm()

    all_post = Board.objects.all()
    context = {'take_all_post':all_post}
    return render(request, 'createpost.html', context)

def board(request):

    return render(request, 'board.html')

def post(request, post_id):
    my_post = Board.objects.get(pk=post_id)

    return render(request, 'post.html', {'my_post':my_post})

# def iscorrect(request):
#     if pw == Board.password:
        
#     return render()    