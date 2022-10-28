from django.db import models

# Create your models here.

'''
리뷰 목록 
- 리뷰 제목 (title)
- 리뷰 내용 (content)
- 영화 이름 (movie_name)
- 영화 평점 (grade)
- 리뷰 생성시간(created_at)
- 리뷰 수정시간(updated_at)
'''

class Review(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.TextField()
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)