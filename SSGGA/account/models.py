from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:                                                 
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # pass # superuser 생성할때 하세용 ~
    instance.profile.save()


class Profile(models.Model):
    M_or_F = (
    ('남', '남'),
    ('여', '여'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=5)
    nickname = models.CharField('닉네임', max_length=20, null=True)
    birth = models.DateField('생년월일', null=True)
    phone = models.CharField('전화번호', max_length=20)
    gender = models.CharField('성별', choices=M_or_F, max_length=2)
    email = models.EmailField('이메일', max_length=254)
    image = models.ImageField('(선택) 프로필사진', null=True, default="./images/userdefaultimg.png")

    def __str__(self):
        return self.name