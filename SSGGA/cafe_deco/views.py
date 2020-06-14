from django.shortcuts import render, redirect, get_object_or_404
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

def cafe_main(request, cafe_id):
    try:
        # user정보 받기
        user = request.user
        profile = user.profile
        ## 요까지

        all_post = Board.objects.all()

        thisuser = request.user

        cafe = get_object_or_404(Cafe, pk=cafe_id)
        adminuser = cafe.adminuser

        image_obj = BannerImage.objects.filter(cafe=cafe).last()
        url = image_obj.image.url if image_obj else ""

        if thisuser==adminuser:
            isAdmin = True
        else:
            isAdmin = False

        context ={'image': url, 'isAdmin':isAdmin, 'profile':profile, 'all_post':all_post, 'cafe':cafe}

    except Exception:
        # user 정보 없으면 걍 받지말기

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

        context ={'image': url, 'isAdmin':isAdmin, 'all_post':all_post, 'cafe':cafe}

    return render(request, 'cafe_main.html', context)

def cafe_setting(request, cafe_id):
    if request.method == "GET":
        banner_form = BannerForm()

        banner_image_obj = BannerImage.objects.last()
        if banner_image_obj:
            banner_img = banner_image_obj.image.url
        else:
            banner_img = ""

        try:
            cafe = Cafe.objects.get(pk=cafe_id)
        except Cafe.DoesNotExists:
            cafe = None

        return render(request, 'cafe_setting.html', {
            'banner_form': banner_form,
            'banner_image': banner_img,
            'cafe': cafe,
        })
    elif request.method == "POST":
        banner_form = BannerForm(request.POST, request.FILES)
        cafe = get_object_or_404(Cafe, pk=cafe_id)

        if banner_form.is_valid:
            banner = banner_form.save()
            banner.cafe = cafe
            banner.save()
        
        return redirect("cafe_main", cafe_id)

def bulletinboard_page(request, cafe_id):
    try:
        user = request.user
        profile = user.profile

        all_post = Board.objects.all()

        banner_image = load_banner_img()

        cafe = Cafe.objects.get(pk=cafe_id)

        return render(request, 'bulletinboard_page.html', {
            'all_post': all_post,
            'profile': profile,
            'banner_image' : banner_image,
            'cafe':cafe,
        })
    except:
        all_post = Board.objects.all()

        banner_image = load_banner_img()

        cafe = Cafe.objects.get(pk=cafe_id)

        return render(request, 'bulletinboard_page.html', {
            'all_post': all_post,
            'banner_image' : banner_image,
            'cafe':cafe,
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
