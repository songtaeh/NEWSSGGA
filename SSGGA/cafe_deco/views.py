from django.shortcuts import render, redirect
from .forms import BannerForm
from .models import BannerImage
from board.models import Board
from account.models import Profile
from cafeapp.models import Cafe

# Create your views here.
def load_banner_img():
    banner_image_obj = BannerImage.objects.last()
    if banner_image_obj:
        return  banner_image_obj.image.url
    else:
        return  ""

# def user_account(request):
#     user_info = Profile.objects.all()
#     name = user_info.name
#     nickname = user_info.nickname
#     image = user_info.image

#     return render(request, 'cafe_main.html', {'user_info':user_info})

def cafe_main(request, cafe_id):
    
    user = request.user
    profile = user.profile
    all_post = Board.objects.all()
    image_obj = BannerImage.objects.last()

    if image_obj:
        url = image_obj.image.url
    else:
        url = ""

    thisuser = request.user

    cafe = Cafe.objects.get(pk=cafe_id)
    adminuser = cafe.adminuser

    if thisuser==adminuser:
        isAdmin = True
    else:
        isAdmin = False
        
    context ={'image': url, 'isAdmin':isAdmin, 'profile':profile, 'all_post':all_post}

    return render(request, 'cafe_main.html', context)

    # welcome_image_obj = WelcomImage.objects.last()
    # if image_obj:
    #     welcome_img = welcome_image_obj.image.url
    # else:
    #     welcome_img = ""

    # return render(request, 'cafe_main_admin.html', {
    #     'welcome_image': welcome_img,
    # })

def cafe_setting(request):
    if request.method == "GET":
        banner_form = BannerForm()

        banner_image_obj = BannerImage.objects.last()
        if banner_image_obj:
            banner_img = banner_image_obj.image.url
        else:
            banner_img = ""

        return render(request, 'cafe_setting.html', {
            'banner_form': banner_form,
            'banner_image': banner_img,
        })
    elif request.method == "POST":
        banner_form = BannerForm(request.POST, request.FILES)
        if banner_form.is_valid:
            banner_form.save()

    # if request.method == "GET":
    #     welcome_image_form = WelcomeImageForm()

    #     welcome_image_obj = WelcomeImage.objects.last()
    #     if welcome_image_obj:
    #         welcome_img = welcome_image_obj.image.url
    #     else:
    #         welcome_img = ""

    #     return render(request, 'cafe_setting.html', {
    #         'welcome_image_form': welcome_image_form,
    #         'welcome_image': welcome_img,
    #     })
    # elif request.method == "POST":
    #     welcome_image_form = WelcomeImageForm(request.POST, request.FILES)
    #     if welcome_image_form.is_valid:
    #         welcome_image_form.save()

    user_info = Profile.objects.all()

    all_post = Board.objects.all()
    
    return redirect("cafe_main", {'user_info':user_info, 'all_post':all_post})

def bulletinboard_page(request):

    all_post = Board.objects.all()

    user = request.user
    profile = user.profile

    banner_image = load_banner_img()

    return render(request, 'bulletinboard_page.html', {
        'all_post': all_post,
        'profile': profile,
        'banner_image' : banner_image,
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
