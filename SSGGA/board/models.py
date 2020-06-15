from django.db import models
from cafeapp.models import Cafe


class Board(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete = models.CASCADE, # 글이 지워지면, 댓글도 함께 지워라
        # related_name = "blogcomment"    #comment_set 대신, blogcomment라는 이름으로 할 수 있음. 추가적인 옵션
        # default = Cafe.objects.get(id=1),
        # default = "null"
        null=True
    )

    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=4)   # pw는 4자리
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # imageload = models.ImageField(default="null") # 자소설 모델인데, 이미지 받으려고 작성한 필드
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title