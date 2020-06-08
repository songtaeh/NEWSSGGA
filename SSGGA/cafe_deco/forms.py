from django import forms
from .models import BannerImage


class BannerForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ["image"]
