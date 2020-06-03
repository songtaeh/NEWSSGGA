from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    
    class Meta:
        model = Cafe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Explain'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "카페를 설명해주세요.",
            'rows': 10,
            'cols': 89})
