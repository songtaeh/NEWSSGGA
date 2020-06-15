from django.db import models
from django.conf import settings

class Cafe(models.Model):
    title = models.CharField('카페명',max_length=100)
    explain = models.TextField('카페 설명',max_length=1000, null=True)
    tag = models.CharField('태그',max_length=30)
    secret = models.BooleanField('공개여부')
    cafe_icon = models.ImageField('카페 아이콘', upload_to='images/', null=True, default="images/user_default_img.png")
    adminuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


# Create your models here.