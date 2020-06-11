from django.db import models
from django.conf import settings

class Cafe(models.Model):
    title = models.CharField('카페명',max_length=100)
    explain = models.TextField('카페 설명',max_length=1000, null=True)
    tag = models.CharField('태그',max_length=30)
    secret = models.BooleanField('공개여부')
    image = models.ImageField('카페 아이콘', null=True, default="./images/userdefaultimg.png")
    adminuser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


# Create your models here.
