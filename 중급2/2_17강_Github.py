# 깃헙에올릴떈 imcvtP폴더만 있음된다.

"""
chapter 4
pyton Advanced(4) - 나만의 패키지 만들기(1)
Keyword - Github,  package deploy

"""

"""
패키지 배포 순서(Github)
1. https://github.com/
2. 이때 잘만들어진 .gitignore 를 정리해논 파일이 있음.
==============================================
2. 기존 만들어논 upload_package가져오기
3. 우리가만든 py_ad_2_17파일을 복사해서 imcvtP파일 에 붙여넣기
(이때 imcvtP파일 내부의 gitignore, license, manifest, readme, requirement,setup.cfg, setup.py
이것들은 강사님이 준비해주심.)
안의 파일은 하나하나 다읽어보기.
-> gitignore : 보통 pypi와 깃헙 두곳에 패키지를 배포하는걸 원칙으로함.
   이때 github에서 다운받는사람이 불필요한 파일까지내려받지 않도록 예외 조건 지정
   인터넷 처보면 세팅된 내용 받을 수 있음.
-> Licencse : MIT 라이센스로 되어 있음. https://blog.naver.com/occidere/220850682345 참고
-> MANIFEST : 설치할떄 LICENSE, README, reauirment 를 가져가세요 라고 명시한다.
-> Setup.py 파일이 중요. 여기에도 다른 패키지와 겹치지 않게 name 지정, install_requires에 패키지명을넣으면
   자동으로 이 패키지 받을때 자동 설치됨.
   find_packages() 는 imcvtP에서 패키지를 찾게됨.
   Keywords 로 지정하면 이 단어로 검색시 내 패키지가 검색됨.
   Classifiers도 형식이 있다.
   setup.cfg는 불필요한 파일배제, 꼭가져가야될 파일을 명세 지정.
   요 6개(License, MANIFEST, README, requirement, setup.cfg(없어도됨),setup.py는 늘 반드시 필요하다. 
4. imcvtP파일에 __init__ 이라는 py 파일 하나더 만들기
5. pip install setuptools wheel > 짐을 싸주는 패키지
wheel 설치 후 빌드 업-> 설치판 생성 -> cmd 창으로 이동
-> 설치시 배포할 폴더들(setup.py)와 같은 경로에 pip install 해줘야 함
-> 설치1 : python -m pip install --upgrade setuptools wheel
-> 설치2 : python -m pip install --user --upgrade setuptools wheel
6. 빌드 : python setup.py sdist bdist_wheel
7. 설치된 파일들어가서 잘들어갔는지압축파일 확인

여기까지 pypi랑 같음
=====================================================
3. git 설치 확인
4. gid add -> commit -> push 
 - git repository 저장소 생성
 - git init
 - git add .
 - git status
 - git commit -m 'message'
 - git remote add origin 'your repository'
 
5. pypi에서 활용했던 upload_package 폴더로 cmd로 이동. 
 dir 입력 후 Licence, readme 등이 있어야 함.
 
6. PyPi 형태의 패키지 구조를 github repository에 push
7. 설치 확인(pip install git+https://your-reposioory-url)

"""

from imcvtP.converter import GifConverter 
path_in = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/images/*.png'
path_out = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/image_out/result.gif'

# 클래스 생성
# 클래스
c = GifConverter(path_in, path_out,(320,240))
# 반환
c.convert_gif()