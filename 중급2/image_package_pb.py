"""
chapter 4
pyton Advanced(4) - 나만의 패키지 만들기(1)
Keyword - PyPI, build, package deploy
"""

# py_ad_2_17 완성된 패키지 임포트

from py_ad_2_17 import GifConverter as gfc
path_in = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/images/*.png'
path_out = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/image_out/result.gif'

# 클래스 생성
# 클래스
c = gfc(path_in, path_out,(320,240))
# 반환
c.convert_gif()

"""
패키지 배포 순서(PyPI)

1. https://pypi.org 회원가입
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

8. PyPi 배포
 -> 설치 : pip install twine (이걸사용하라고 권장함)
 -> 업로드 : python -m twine upload dist/* dist폴더 안에 있는 모든 폴더를 업로드해줘
 
9. 그러면 API 키를 입력하라고 뜰것이다. 그러면 Your project > account setting > API tokens
들어가서 2단계인증까지해주면 된다.(구글인증 활용함)

10. 그후 키를 카피한다음 API 인증하라는 cmd 에 마우스 오른쪽 버튼 한번만 눌러주고 
엔터 누르면된다. (키가 안나옴) -> 주의! 토큰 키는 복사해서 고이 잘 모셔두자.

 -동일한 이름의 패키지가 업로드되면 유저이름으로 업로드가허용이안된다는 메시지가뜸

11. 이로서 Pypi에 올리는건 끝

12. 수정할 사항이 생기면 수정한 뒤

13. 다시 빌드 : python setup.py sdist bdist_wheel
 -> 업로드 : python -m twine upload dist/* dist폴더 안에 있는 모든 폴더를 업로드해줘
 

14. 설치 확인 (pip install imcvtP)
from imcvtP.converter import GifConverter as 
"""
path_in = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/images/*.png'
path_out = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/image_out/result.gif'

from imcvtP.converter import GifConverter 


# 사용자 접근예시
# import 했으므로 GifConverter를 먼저 찾아봄
print(dir(GifConverter))

# 클래스
c = GifConverter(path_in, path_out,(320,240))
# 이 c가 뭐지?
c.__doc__
# 안나오네, 그럼 한번 더 접근해볼까 -> 한글떄문에 안나오는것으로 추정됨
dir(c)
# convert_gif라는 얘를 한번 실행해봐야겠다. 
c.convert_gif()

