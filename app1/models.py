from django.db import models


# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기 -> 이설정을 하지 않으면 목록에서 글 제목이 Postobject(1), Postobject(2) 이런식으로 노출됨.
    def __str__(self):
        return self.postname
