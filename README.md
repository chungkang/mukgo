# MukGo: 먹방에 대한 고찰

## Set Development Environment
### 1. Install Python 3.7.6
<https://www.python.org/downloads/release/python-376/>

### 2. Install Git
<https://git-scm.com/>

### 3. Set Python 'Virtual Environments'
<http://pythonstudy.xyz/python/article/302-%EA%B0%80%EC%83%81-%ED%99%98%EA%B2%BD>

#### 3.1. Set Virtual Environmnets
##### Mac OS
    . ~/venv1/bin/activate

##### Windows OS
    C:\Python35> python Tools\scripts\pyvenv.py C:\PyEnv\venv1

#### 3.2. Activate Virtual Environments
##### Mac OS
    . ~/venv1/bin/activate
    
##### Windows OS
    C:\PyEnv\venv1> Scripts\activate.bat
            
### 4. Install Django on 'Virtual Environments'
<http://pythonstudy.xyz/python/article/303-Django-%EC%84%A4%EC%B9%98>

#### 4.1. Install 'Django'
    (venv1)$ pip install django
    
    Django Version: 3.0.2

#### 4.2. Install 'django_heroku'
    (venv1)$ pip install django_heroku

### 5. Clone the Project from Github and Run Local Server
#### 5.1. Fork the remote repository to your repository
#### 5.2. Clone the project from your remote forked repository
<https://recoveryman.tistory.com/257>


PyCharm 설치
https://www.jetbrains.com/pycharm/
	해당 프로젝트 열기 > requirements.txt에 있는 dependencies 설치


가상환경 activate
. ~/venv1/bin/activate 

윈도우에서 가상환경 실행
C:\PyEnv\venv1> Scripts\activate.bat




로컬 서버 실행
해당 프로젝트 root로 진입
(가상환경) ./manage.py runserver
혹은
(가상환경) python3 manage.py runserver




참고 자료
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
