from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    
    class Meta:
        model = Cafe
        fields = ['title', 'explain', 'tag', 'secret', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['explain'].widget.attrs.update({
            'class': 'form_explain',
            'rows': 5,
            'cols': 30})

        self.fields['title'].label = "카페명 "
        self.fields['image'].label = "카페 아이콘 "
        self.fields['explain'].label = "카페 설명 "
        self.fields['secret'].label = "공개 여부 "
        self.fields['tag'].label = "태그 "

        self.fields['title'].widget.attrs.update({
            'class': "form_title"})    
        self.fields['tag'].widget.attrs.update({
            'class': "form_tag"})  
        self.fields['secret'].widget.attrs.update({
            'class': "form_secret"
        })       
        self.fields['image'].widget.attrs.update({
            'class': "form_image"})  



