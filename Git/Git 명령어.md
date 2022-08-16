# Git 명령어

* git add : 수정된 소스코드들을 Staging Area로 전달
* git commit : add된 모든 소스코드들을 Local Repository로 전달
* git push : LocalRepository에서 변경이 발생한 파일들을 RemoteRepository로 전달
* git pull : RemoteRepository에서 변경이 발생한 파일들을 Local PC에 있는 모든 공간에 전달
* git fetch : RemoteRepository의 변경이 발생한 파일들을 LocalRepository에 전달 (fetch를 하더라도 IDE 등의 작업공간에는 변경사항이 적용되지 않음)
* git merge : LocalRepository에서 변경이 발생한 파일들을 WorkingDirectory로 전달 (IDE 등의 작업공간에 변경사항이 적용)
* git init : RemoteRepsitory와 연동하기 위해 가장 먼저 수행되는 초기화 작업
* git branch : 생성되어 있는 브랜치를 확인
* git branch {name} : name의 이름으로 새로운 브랜치를 생성
* git checkout {name} : 현재 브랜치를 name으로 변경
* git status : WorkingDirectory에서 수정이 발생된 파일들을 확인
* git clone : RemoteRepository에 저장되어 있는 모든 파일들을 Local PC에 복사 (서버와 로컬 간 연동도 되어있음)
* git reset {soft/mixed/hard }: 작업된 파일들을 특정 커밋 위치로 리셋