from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    ID = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birth = forms.DateField(required=True)  # 포맷
    gender = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        # fields = ("username", "email")
        fields = ("ID", "password1", "password2", "username", "birth", "gender", "phone")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.ID(self.cleaned_data["ID"])
        user.email(self.cleaned_data["email"])
        user.birth(self.cleaned_data["birth"])
        user.gender(self.cleaned_data["gender"])
        user.phone(self.cleaned_data["phone"])

        if commit:
            user.save()
        return user