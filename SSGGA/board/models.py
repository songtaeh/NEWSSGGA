from django.db import models

# Create your models here.

class Board(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=4)   # pw는 4자리
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # imageload = models.ImageField(default="null") # 자소설 모델인데, 이미지 받으려고 작성한 필드
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title