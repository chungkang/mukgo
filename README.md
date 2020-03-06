# MukGo: 먹방에 대한 고찰

## 개발 환경 설정
### 1. PC 설치 항목
#### a. 파이썬 3.7.6 설치
<https://www.python.org/downloads/release/python-376/>

#### b. Git 설치
<https://git-scm.com/>

#### c. PyCharm 설치
<https://www.jetbrains.com/pycharm/>

### 2. 계정 생성 항목
#### a. Github 계정 생성
www.github.com

### 3. Python 가상 환경 설정
#### a. Python Virtual Environmnet 생성
<http://pythonstudy.xyz/python/article/302-%EA%B0%80%EC%83%81-%ED%99%98%EA%B2%BD>
	
파이썬 설치한 경로에서 실행

Mac OS

	pyvenv ~/venv1
	python3.7 -m venv ~/venv2

Windows OS

	C:\Python35> python Tools\scripts\pyvenv.py C:\PyEnv\venv1
	C:\>c:\Python35\python -m venv c:\path\to\venv1

#### b. Activate Virtual Environment
파이썬 설치한 경로에서 실행

Mac OS

	. ~/venv1/bin/activate

Windows OS

	C:\PyEnv\venv1> Scripts\activate.bat

#### c. 가상 환경에 Django 설치
<http://pythonstudy.xyz/python/article/303-Django-%EC%84%A4%EC%B9%98>

	pip install django

### 4. 로컬 개발환경 설정
#### a. Gihub 개인 계정에서 https://github.com/chungkang/mukgo 프로젝트 fork

#### b. fork한 프로젝트 로컬로 clone
	git clone 'fork한 프로젝트 URL'
ex) git clone https://github.com/MukGo/mukgo.git
		
#### c. 프로젝트에서 필요한 라이브러리 설치
가상환경에서 해당 프로젝트 root 디렉토리 진입

	pip install -r requirements.txt
		
#### d. 로컬 서버 가동
프로젝트 root 디렉토리 진입

	./manage.py runserver

### 5. Github를 사용한 협업 방법
Git의 사용법에 대해서는 '누구나 쉽게 이해할 수 있는 Git 입문' 참고
<https://backlog.com/git-tutorial/kr/>

#### a. branch 생성
자신의 브랜치 확인

	git branch
	
개발 일감에 맞는 브랜치 생성

	git branch <branchname>
		
브랜치 전환

	git checkout <branchname>
	
#### b. 로컬에서 commit 하고 원격 저장소로 push하기
PyCharm을 에서 개발 개발

git staging 확인

	git status

개발한 내용 add

	git add 작업파일명
	(전체를 add 할 경우) git add .

개발한 내용 commit

	git commit -m "설명을 추가"
		
#### c. 자신의 원격 저장소에 push
해당 브랜치 자신의 원격 저장소로 push

	git push --set-upstream origin 브랜치명
		
자신의 깃허브 해당 원격 저장소에서 Compare&pull request 클릭하여 upstream 저장소로 전송



## 참고 자료
Django 프로젝트 이해
http://pythonstudy.xyz/python/article/301-Django-%EC%86%8C%EA%B0%9C
https://wikidocs.net/6600

웹에 대한 이해
https://opentutorials.org/course/1688/9334
https://opentutorials.org/course/1688/9408

Python pip 패키지 관리자
http://pythonstudy.xyz/python/article/504-pip-%ED%8C%A8%ED%82%A4%EC%A7%80-%EA%B4%80%EB%A6%AC%EC%9E%90

Git 이란
https://opentutorials.org/course/307/2475


Github 
https://github.com/

Github 사용법
https://backlog.com/git-tutorial/kr/intro/intro2_4.html
