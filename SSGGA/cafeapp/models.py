from django.db import models

class Cafe(models.Model):
    title = models.CharField('카페명',max_length=100)
    explain = models.TextField('카페 설명',max_length=1000)
    tag = models.CharField('태그',max_length=30)
    secret = models.BooleanField('공개여부')
    image = models.ImageField('카페 아이콘', null=True, default="./images/userdefaultimg.png")

    def __str__(self):
        return self.title


# Create your models here.
