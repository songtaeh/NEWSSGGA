from django.shortcuts import render, redirect
from cafeapp.models import Cafe
from django.http import Http404
from django.contrib.auth.models import User
from account.models import Profile
from .models import Board
from .forms import BoardForm
# Create your views here.
# def cafemain(request, cafe_id):
#     try :
#         i = Cafe.objects.get(pk=cafe_id)
#         user = request.user
#         p = user.profile

#         context = {'i':i, 'p':p}
#     except :
#         i = Cafe.objects.get(pk=cafe_id)
#         context = {}
#     return render(request,'cafe_main.html', context)

# 수정 완료
def createpost(request, cafe_id):
    try:
        user = request.user
        profile = user.profile
        
        all_post = BoardForm(request.POST)

        image_obj = BannerImage.objects.filter(cafe=cafe).last()
        url = image_obj.image.url if image_obj else ""

        if all_post.is_valid():
            temp = all_post.save(commit=False)
            temp.cafe = Cafe.objects.get(id=cafe_id)
            temp.save()

            return redirect('/bulletinboard_page/{}'.format(cafe_id))

        all_post = BoardForm(request.GET)

        context = {'image':url, 'all_post':all_post, 'profile':profile}
        return render(request, 'createpost.html', context)
    except:
        all_post = BoardForm(request.POST)

        image_obj = BannerImage.objects.filter(cafe=cafe).last()
        url = image_obj.image.url if image_obj else ""

        if all_post.is_valid():
            temp = all_post.save(commit=False)
            temp.cafe = Cafe.objects.get(id=cafe_id)
            temp.save()

            return redirect('/bulletinboard_page/{}'.format(cafe_id))

        all_post = BoardForm(request.GET)

        context = {'image':url, 'all_post':all_post}
        return render(request, 'createpost.html', context)

def deletepost(request, cafe_id, post_id):
    image_obj = BannerImage.objects.filter(cafe=cafe).last()
    url = image_obj.image.url if image_obj else ""

    return redirect('/bulletinboard_page/{}'.format(cafe_id))  


def update(request, cafe_id, post_id):
    try:
        user = request.user
        profile = user.profile

        image_obj = BannerImage.objects.filter(cafe=cafe).last()
        url = image_obj.image.url if image_obj else ""

        my_post = Board.objects.get(pk=post_id)
        if request.method == "POST":
            update_form = BoardForm(request.POST, instance=my_post)
            if update_form.is_valid():
                print('11111111111111111')
                update_form.save()

            return redirect('/bulletinboard_page/{}'.format(cafe_id))
            # 검사를 꼭 해주어야 save를 사용할 수 있다.
        # object를 안에다가 넣어준다
        update_form = BoardForm(instance=my_post)

        return render(request, 'update.html', {'image':url, 'update_form': update_form, 'my_post': my_post, 'profile':profile})    
    except:
        image_obj = BannerImage.objects.filter(cafe=cafe).last()
        url = image_obj.image.url if image_obj else ""

        my_post = Board.objects.get(pk=post_id)
        if request.method == "POST":
            update_form = BoardForm(request.POST, instance=my_post)
            if update_form.is_valid():
                update_form.save()

            return redirect('/bulletinboard_page/{}'.format(cafe_id))
            # 검사를 꼭 해주어야 save를 사용할 수 있다.
        # object를 안에다가 넣어준다
        update_form = BoardForm(instance=my_post)

        return render(request, 'update.html', {'image':url, 'update_form': update_form, 'my_post': my_post})    

# def board(request):

#     return render(request, 'board.html')    

def post(request, cafe_id, post_id):
    try:
        user = request.user
        profile = user.profile

        cafe = Cafe.objects.get(pk=cafe_id)
        
        my_post = Board.objects.get(pk=post_id)

        # image_obj = BannerImage.objects.filter(cafe=cafe).last()
        # url = image_obj.image.url if image_obj else ""


        return render(request, 'post.html', {'my_post':my_post, 'cafe':cafe, 'profile':profile})
    except:
        cafe = Cafe.objects.get(pk=cafe_id)
        
        my_post = Board.objects.get(pk=post_id)

        return render(request, 'post.html', {'my_post':my_post, 'cafe':cafe})