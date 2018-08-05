from django.db import models
from django.utils import timezone


# Create your models here.

# 클래스명은 항상 대문
# 블로그글 포스팅하는 클래스 작성
class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # 포스트 객체가 생성되는 시점의 시간
    created_date = models.DateTimeField(default=timezone.now)
    # publish 되는 시간은 공백으로
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        # 작성완료시 해당 시간 설정
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title