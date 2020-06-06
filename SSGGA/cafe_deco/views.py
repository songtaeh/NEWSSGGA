from django.shortcuts import render, redirect
from .forms import BannerForm
from .models import BannerImage

# Create your views here.

def cafe_main(request):

    return render(request, 'cafe_main.html')

def cafe_main_admin(request):

    return render(request, 'cafe_main_admin.html')

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
            return redirect("cafe_setting")

def bulletinboard_page(request):

    return render(request, 'bulletinboard_page.html')

def change_save(request):
    return redirect("cafe_main")