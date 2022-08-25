from django.db import models

# Genre 클래스를 만드는데,
# models.Model 내부 클래스를 상속 받는다. 
# 왜 상속 받을까요? 기능들을 활용하고 싶어서. (미리 만들어진)
class Genre(models.Model):
    name = models.CharField(max_length=30)

class Artist(models.Model):
    name = models.CharField(max_length=30)
    debut = models.DateField()

# Genre는 Album을 0~여러개 가진다. / Album은 하나의 Genre를 가짐
# 예) 트로트 -> 네박자, .... 
# Artist는 Album을 0~여러개 가진다. / Album은 한명의 가수를 가짐
# 예) BTS -> Butter, ....
class Album(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

