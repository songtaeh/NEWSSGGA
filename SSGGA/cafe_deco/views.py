from django.shortcuts import render, redirect
from .forms import BannerForm
from .models import BannerImage
from board.models import Board
from account.models import Profile
from cafeapp.models import Cafe

# Create your views here.

def cafe_main(request, i_id):
    image_obj = BannerImage.objects.last()
    i = Cafe.objects.get(pk=i_id)
    if image_obj:
        url = image_obj.image.url
    else:
        url = ""

    return render(request, 'cafe_main.html', {"image": url, "i":i})

def cafe_main_admin(request):

    image_obj = BannerImage.objects.last()
    if image_obj:
        url = image_obj.image.url
    else:
        url = ""

    return render(request, 'cafe_main_admin.html', {
        "image": url    
    })

def cafe_setting(request):
    if request.method == "GET":
        form = BannerForm()

        image_obj = BannerImage.objects.last()
        if image_obj:
            url = image_obj.image.url
        else:
            url = ""

        return render(request, 'cafe_setting.html', {
            'form': form,
            'image': url,
        })
    elif request.method == "POST":
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("cafe_main")

def bulletinboard_page(request):
    all_post = Board.objects.all()

    user = request.user
    if user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None

    image_obj = BannerImage.objects.last()
    if image_obj:
        url = image_obj.image.url
    else:
        url = ""

    return render(request, 'bulletinboard_page.html', {
        'all_post': all_post,
        'profile': profile,
        'image' : url,
    })

# def mypost(request):
#     posts = Board.objects.all()
#     profile = None
#     user = request.user
#     if user.is_authenticated:
#         posts = posts.filter(nickname=request.user.profile.nickname)
#         profile = request.user.profile

#     return render(request, 'mypost html 추가예정', {
#         'all_post': posts,
#         'profile': profile,
#     }

def user_account(request):
    user_info = Profile.objects.all()
    name = user_info.name
    nickname = user_info.nickname

    return render(request, 'cafe_main.html', {'user_info':user_info})
