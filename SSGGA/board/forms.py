from django import forms
from .models import Board
from django.contrib import admin

class BoardForm(forms.ModelForm):
    
    # 메타 클래스란 클래스 안에 선언해서 상위의 클래스에게 메타데이터, 즉 옵션이나 데이터를 추가해줄 수 있는 것
    class Meta:
        model = Board
        fields = ('nickname', 'password', 'title', 'contents')

        # fields = ('title', 'body')

class BoardAdmin(admin.ModelAdmin):
    readonly_fields=('help_num',)
    form = BoardForm