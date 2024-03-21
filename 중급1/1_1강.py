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

# 객체 지향 프로그램(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리
# 데이터 분석, 크롤링 등을 이용할 땐 절차 지향으로 해도 됨.

# 일반적인 코딩 
# 자동차들을 관리하는 코드를 짜준다하자.

#차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color':'White'},
    {'horsepower':400},
    {'price' : 8000}
]

# 만약 차량이 하나 더 추가된다면
car_company_2 = 'BMW'
car_detail_2 = [
    {'color':'Black'},
    {'horsepower':270},
    {'price' : 5000}
]

car_company_3 = 'Audi'
car_detail_3 = [
    {'color':'Silver'},
    {'horsepower':300},
    {'price' : 6000}
]

# 리스트 구조

car_company_list = ['Ferrai', 'Bmw', 'Audi'] #리스트는 순서를 유지하고 인덱스로 접근가능
car_detail_list = [
    {'color':'White','horsepower':400,'price' : 8000},
    {'color':'Black','horsepower':270,'price' : 5000},
    {'color':'Silver','horsepower':300,'price' : 6000}
]
# 리스트 구조의 불편함 : 
#  1. 관리하기가 불편, 만약 Bmw가 망했다면 Bmw와 관련된 것들도 지워주거나 이를 관리하는 함수를 따로 만들어야 됨.
#  2. 삭제하려면 인덱스번호를 알아야 함.
# 휴먼에러 : 인덱스 접근 시 실수 가능성

del car_company_list[1]
del car_detail_list[1]
print(car_company_list)
print(car_company_list)

# 물론 각 목적에 맞는 패키지들도 존재한다.

# 딕셔너리 구조
# 코드 반복 지속.. 딕셔너리에서는 키가 중첩이 불가하나 중첩문제가 발생함
# 키 조회 예외 처리 등
# 딕셔너리의 머신러닝 과정의 소스를 보면 딕셔너리는 정말 많이 쓰임.
# 딕셔너리로 수천, 수백만 자료를 다룬다.
# 카 딕셔너리 안에 또 딕셔너리가 있는 형태
car_dicts = [
    {'car_company': 'Ferrai', 'car_detail': {'color':'White','horsepower':400,'price' : 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color':'Black','horsepower':270,'price' : 5000}},
    {'car_company': 'Audi', 'car_detail': {'color':'Silver','horsepower':300,'price' : 6000}}
]

print(car_dicts)
# 지울때 pop이나 del 활용가능
# pop(key, 'default')
del car_dicts[1]
print(car_dicts)

#차량이 증가될수록 코딩의 양이 계속 늘어나게 됨.
#이런 절차 지향에서 class 기반으로 페러다임이 옮겨가는 과정을 보이겠다.

#class 형태로 재구성 해보자.
# 구조 설계 후 재사용성 증가, 코드 반복 최소화

class Car():
    # 기본적인 init이 있어 실행해도 에러발생 안됨
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # __str__ 통해 원하는 클래스 인스턴스 내부의 속성 정보를
    # 내가 원하는 방식으로 출력이 가능하다.
    def __str__(self): 
        return 'str {} - {}'.format(self._company, self._details)

    #__str__ 는 print를 보는 사용자 입장에서 볼때,
    # __repr__는 개발자관점에서 객체고 이 자료형의 타입에 따른 개체를 그대로 표시해줄 때
    # 만약 둘다 사용했을 때 str이 없다면 repr를 출력한다.
    # 둘다 없을 경우 상위정보인 랩핑된 정보만 나옴
    # 두개 다 선언해놓고 보는것도 좋은 방법이다.
    def __repr__(self): 
        return 'repr {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari',{'color':'White','horsepower':400,'price' : 8000})
car2 = Car('Bmw',{'color':'Black','horsepower':270,'price' : 5000})
car3 = Car('Audi',{'color':'Silver','horsepower':300,'price' : 6000})


print(car1)
print(car2)
print(car3)

# __dict__를 사용하면 이안의 attribute(속성) 값들을 다 볼 수 있게 된다.
# _company, _detail이 나옴
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

#dir함수로 만들어둔 클래스 이름을 실행하면 활용가능한 메타정보가 다나온다.
# 차후 중요한 정보들은 다 할 예정
print(dir(car1))

# 이렇게 인스턴스를 관리할 때 리스트로 관리가 가능하다.

car_list= []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 리스트로 append하여 실행했을 경우 str이 아닌 repr 정보가 출력된다.
print(car_list)

# for문으로 해서 프린트할 경우에는 str로 출력된다.
for x in car_list :
    print(x)
    # 명시적으로 repr를 지정해주면 repr가 출력이 된다
    print(repr(x))