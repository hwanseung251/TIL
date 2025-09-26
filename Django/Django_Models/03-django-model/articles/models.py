from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 이름이 파스칼케이스? -> 클래스
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)