import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 1. Artist 생성
import datetime 
artist = Artist() 
artist.name = '아이브'
# 2021년 12월 1일
artist.debut = datetime.date(2021, 12, 1)
artist.save()

artist = Artist() 
artist.name = '아이유'
artist.debut = '2019-12-26'
artist.save()

# 1:N 관계에서의 Create

# 객체
# Class 정의를 genre로 했기 때문
album = Album()
album.name = '꽃'
# album.genre = 1
# ValueError: Cannot assign "1": "Album.genre" must be a "Genre" instance.       
genre = Genre.objects.get(id=1)
album.genre = genre
artist = Artist.objects.get(id=1)    
album.artist = artist
album.save()

# 값
# 테이블에 실제 필드는 _id가 붙어있기 때문
album = Album()
album.genre_id = 1
album.artist_id = 1
album.name = '미아'
album.save()

# N => 1 (참조)
# 앨범의 id가 1인 것의
album = Album.objects.get(id=1) # 앨범 객체
# 장르의 이름은..?
album.genre # 장르 객체
# <Genre: Genre object (1)>
album.genre.name
# '발라드'


# 1 => N (역참조)
# 클래스이름_set
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id=1)
g1.album_set.all() 
# <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>