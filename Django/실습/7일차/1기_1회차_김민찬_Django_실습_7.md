# Django CRUD 

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

## 2. articles app 

### 1. app 생성

```bash
python manage.py startapp [앱 이름]
```

### 2. app 등록

settings.py에 '앱 이름' 추가

### 3. urls.py 설정 

from django.urls import include
path('articles/', include('articles.urls')),

## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

models.py에 title, content 등 내용 작성
ex)
모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

### 2. 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

### 3. DB 반영(`migrate`)

```bash
$ python manage.py migrate
```

## 4. CRUD 기능 구현

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 1. HTML Form 제공

> http://127.0.0.1:8000/articles/new/

#### 2. 입력받은 데이터 처리

> http://127.0.0.1:8000/articles/create/

> 게시글 DB에 생성하고 index 페이지로 redirect

### 2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

### 3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/<int:pk>/

### 4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/<int:pk>/delete/

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/<int:pk>/update/