from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class BannerImage(models.Model):
    image = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(1100, 200)], format='JPEG', options = {'quality': 90})

# class MyinfoImage(models.Model):
#     myinfo_image = ProcessedImageField(default='user_default_img.png', upload_to='myinfo_images/', processors = [ResizeToFill(100,100)], format = 'JPEG', options = {'quality': 90 })