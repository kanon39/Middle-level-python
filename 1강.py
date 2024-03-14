## 개발 가상환경 (VirtualEnv) 설정 ##
# vs 코드내 cmd 명령창으로 이동
# 터미널에 python -m venv [가상환경 이름] 지정 -> 이름 : p_study

# 가상환경지정 방법1 #
# p_study 폴더로 이동하여 p_study > Scripts 로 이동
# vscode일 경우 .\activate.bat 입력
# 이 스크립트 내 패키지를 설치하여 다른 프로젝트 진행시 버전 안꼬이게 분리시킴
# 만약 문제 생길시 p_study 폴더를 삭제하면 됨.
# 반대로 가상환경 해제시 deactivate.bat 터미널에 입력

#가상환경지정 방법2 #
# 위 돋보기 클릭 후 >python: select interpreter 클릭
# 이를 클릭하면 컴퓨터에 설치되어있는 모든 파이썬을 다 가져옴
# 딥러닝 용, 기본 용 등등 용도에 따라나눠 쓸 수 있음.
# 만약 여기에 가상환경이 안나오면 enter interpreter path로 들어가서
# 아까 가상환경 설치한 p_study > scrips > python.exe를 설정해준다.


# 테스트 하기 위해서 pip install pendulum : 시간과 날짜 개발시 유용할패키지
# pip list로 설치된 패키지 목록 확인
# 실제 경로에서는 Lib > site-packages로 이동
# 오른쪽 하단에 가상환경을 바꿔갈 수 있다.

print("hello world!")


