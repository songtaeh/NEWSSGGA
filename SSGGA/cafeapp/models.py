from django.db import models

class Cafe(models.Model):
    title = models.CharField('카페명',max_length=100)
    Explain = models.TextField('카페설명',max_length=1000)
    tag = models.CharField('태그',max_length=30)
    secret = models.BooleanField('공개여부')

    def __str__(self):
        return self.title


# Create your models here.
