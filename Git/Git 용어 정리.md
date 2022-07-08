# 로컬
* $ git init - 로컬 저장소 생성
* $ git add <파일명> - 특정 파일/폴더의 변경사항 추가
* $ git commit -m '<커밋메시지>' - 커밋(버전 기록)
* $ git status - 상태 확인
* $ git log - 버전 확인

# 원격
* $ git push origin master
* $ git pull origin master
* $ remote add origin ~~
* $ clone ~~

# 용어
* Working Directory : 개발자의 현재 시점으로 소스코드를 수정하며 개발하는 공간을 의미
* Staging Area : Working Directory에서 작업한 파일을 Local Repository에 전달하기 위해 파일들을 분류하는 공간
* Local Repository : 로컬 저장소이며 작업한 파일들을 저장해두는 내부 저장소 (.git 폴더)
* Remote Repository : 원격 저장소이며 인터넷으로 연결되어 있어 있는 외부 저장소 (웹 페이지에서 보이는 공간)
* Branch : Remote Repository의 현재 상태를 복사하여 master 브랜치와 별개의 작업을 진행할 수 있는 공간 (보통 브랜치를 생성하여 개발을 진행하고 개발을 완료하면 master 브랜치에 병합하여 개발 완료된 소스코드를 합침)
* Head : 현재 작업중인 브랜치의 최근 커밋된 위치
* Index : Staging Area를 의미