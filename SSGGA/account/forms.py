from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username']
        

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "아이디"
        self.fields['password1'].label = "비밀번호"
        self.fields['password2'].label = "비밀번호 확인"
        
        self.fields['username'].widget.attrs.update(
            {'placeholder': '아이디',
             'class': "ac_item"})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': '비밀번호',
             'class': "ac_item",
             'id': "password1"})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': '비밀번호 확인',
             'class': "ac_item",
             'id': "password2"})

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)        

        self.fields['name'].widget.attrs.update(
            {'placeholder': '성명',
            'class': "pf_item",
             'id': "pf_name"})

        self.fields['nickname'].widget.attrs.update(
            {'placeholder': '닉네임',
            'class': "pf_item",
             'id': "pf_nickname"})

        self.fields['birth'].widget.attrs.update(
            {'placeholder': '0000-00-00',
            'class':'pf_item',
             'id': "pf_birth"})

        self.fields['phone'].widget.attrs.update(
            {'placeholder': '010-0000-0000',
             'class': "pf_item",
             'id': "pf_phone"})

        self.fields['gender'].widget.attrs.update(
            {'placeholder': '성별',
            'class':'pf_item',
             'id': "pf_gender",})

        self.fields['email'].widget.attrs.update(
            {'placeholder': '이메일',
            'class':'pf_item',
             'id': "pf_email"})
        
    class Meta:
        model = Profile
        fields = ['name', 'nickname', 'birth', 'phone', 'gender', 'email', 'image']

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['username'].widget.attrs.update(
            {'class': "username_input",
             'placeholder': 'ID',
             'autocomplete':"off"})
        
        self.fields['password'].label = ""
        self.fields['password'].widget.attrs.update(
            {'class': "password_input",
             'placeholder': '비밀번호',
             'autocomplete':"off"})
    
    error_messages = {
        'invalid_login': (
            "일치하는 아이디/비밀번호가 없습니다."
        ),
    }