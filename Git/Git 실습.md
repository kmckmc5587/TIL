# Git 실습

## 0. 사전 설정(PC 최초 한 번)

```bash
$ git config --global user.name 'Github ID'
$ git config --global user.email 'Github Email'
```



## 1. 바탕화면에 TIL 폴더를 만든다.

- TIL 폴더를 열어서 마크다운 정리 파일을 옮긴다.

- VS Code를 연다.



## 2. TIL 폴더에 git 저장소를 만들어준다.

```bash
$ git init
Initialized empty Git repository in C:/Users/김민찬/Desktop/TIL/.git/

(master) $
```



## 3. 커밋을 만든다.

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        20220705_markdown.assets/
        20220705_markdown.md

nothing added to commit but untracked files present (use "git add" to track)
```

```bash
$ git add .
$ git commit -m '마크다운 정리'
```

```bash
$ git log
commit 3c3b184f75465d1172fd01cc6bdbfcac014a0d10 (HEAD -> master)
Author: kmckmc5587 <kmckmc5587@gmail.com>
Date:   Tue Jul 5 16:32:38 2022 +0900

    마크다운 정리
```

```bash
$ git status
On branch master
nothing to commit, working tree clean
```

