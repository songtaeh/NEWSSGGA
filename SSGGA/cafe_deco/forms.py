from django import forms
from .models import BannerImage


class BannerForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ["image"]

# class WelcomeImageForm(forms.ModelForm):
#     class Meta:
#         model = WelcomeImage
#         fields = ['image']