# Django 개발 환경 설정 가이드


## 폴더 생성 / 진입

* mkdir [폴더이름] -> 폴더 생성
ex) mkdir server
* cd [폴더이름] -> 폴더로 진입
ex) cd server


## 가상환경 생성 / 실행

* pip list -> 설치 확인
* python --version -> 파이썬 버전 확인
* python -m venv [가상환경이름]
ex) python -m venv server-venv
* ls -> 내용 확인
* source [가상환경이름]/Scripts/activate
ex) source server-venv/Scripts/activate
* localhost:8000
* deactivate -> 가상환경 종료


## Django LTS 버전 설치

* pip install django(최신 버전 설치)(X)
* pip install django==3.2.13
* pip list
* python --version
* pip --version


## Django 프로젝트 생성

* django-admin -> django를 관리
* django-admin startproject [프로젝트이름][시작경로]
ex) django-admin startproject firstpjt .(현재 폴더)
* ls
ex) firstpjt/ manage.py* server-venv


## Django 실행

* code . -> 현재 있는 폴더 열기
* python manage.py runserver
* localhost:8000