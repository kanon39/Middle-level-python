# 데이터 모델의 마지막 시간
# NamedTuple 설명 : 
# 1. 기계학습, 머신러닝 등 tensorflow 에서 데이터를 원하는데로  가공할 때 쓰임
# 2. 파이썬에서 웹개발할 때 데이터베이스에서 가져온 값을 원하는 형태로 
# 튜플, 딕셔너리, 리스트, 셋 그리고 네임드튜플로 자료구조 형태를 저장할 수 있다.
# 그중에서도 네임드튜플로 저장하면 레이블까지 확인이가능해서 디버깅이 쉬워짐
# 또한 NamedTuple 에서 튜플이기 때문에 유닉한 값을 변경되지 않는값 저장할 떄 유용

# 객체는 파이썬의 데이터를 추상화 합니다.
# 모든 객체는 id와 type으로 표현이가능하며 value로 표시가능하다.

# 일반적인 튜플
# 튜플로 두점사이의 거리를 구하자
# 아래 처럼 입력만 해두면 이게 뭐하려고하는 건지 3자입장에서 분간하기어렵다.
# 이는 뒤의 NamedTuple을 통해 해결이 가능하다.
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2 )
print(l_leng1)

# 이번엔 네임드 튜플로 구해보겠다.
# what is namedtuple in python 을 구글을 검색하면
# 파이썬에서 class와는 다르고  colloctions module 하위에 있고
# 딕셔너리와 같이 키와 value 형태로 맴핑된다.
# 따라서 키또는 index 둘다 접근이 가능한 신기한 형태다.

from collections import namedtuple

# 네임드 튜플 선언
# Point에 네임드 튜플이 선언됨을 알게 됨과 동시에
# 아 pt3는 인덱스와 키 둘다로 접근이 가능하구나 라고 알 수 있다.
# Point 변수에 'Point'를 선언할께
Point = namedtuple('Point', 'x y')
# 클래스 형태로 튜플을 추상화하고 있다.
pt3 = Point(1.0, 5.0) 
pt4 = Point(2.5, 1.5)

print(pt3)
# print(pt3[0])은 print(pt3.x) 와 같다. 즉 index와 키로 접근이가능
# 또한 성능도 좋다.
print(pt4)
# 아래처럼 해도 좋으나 실수할 수 있으므로 
l_leng2 = sqrt((pt3[0]-pt4[0])**2 + (pt3[1]-pt4[1])**2 )
# 아래처럼 키로 진행하는걸 추천한다.
# 눈으로 흐름을 쫓을 때도 편리하다.
l_leng2 = sqrt((pt3.x-pt4.y)**2 + (pt3.y-pt4.x)**2 )

print(l_leng2)

# 네임드 튜플 선언 4가지방법
# 1. 띄어쓰기 방법
Point1 = namedtuple('Point', 'x y')
# 2. 리스트 방법
Point2 = namedtuple('Point', ['x', 'y'])
# 3. 쉼표로 구분
Point3 = namedtuple('Point', 'x, y')
# 이게 중요 >>> 4. 키 중복 또는 class와 같이 예약어가 들어가 있을 경우
# rename=True로 4개의 객체를 받앗다.
# rename의 경우 중복된값이나 예약어가 있을 경우 알아서 변수명을 바꿔준다.
Point4 = namedtuple('Point', 'x y x class', rename=True)

 # 출력
print(Point, Point1, Point2, Point3, Point4 )
 # 딕셔너리를 unpacking 하기
temp_dict = {'x':75, 'y':55}

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10,20,30,40)
 # 딕셔너리의 경우 언패킹할경우 알아서 namedtuple로 된다.
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
# 사용
# p1[0]+p2[1]보다 특정 값으로 접근하는데 namedtuple을 쓴다.
print(p1[0]+p2[1])
print(p1.x + p2.y)

# 아래는 묶여있던 것을 푼 것이다.
x, y = p3
print(x,y)

# 네임드 튜플 메소드
# _make() : 새로운 객체 생성
temp = [52, 38]
p6 = Point1._make(temp) 
print(p6)

# _fields : 필드(키) 네임 확인
print(p1._fields,p2._fields, p3._fields, p4._fields )

# _asdict() : 이건 중요. 정렬된 딕셔너리 반환
# 네임드 튜플을 딕셔너리로 변환하는 것이다.
print(p1._asdict())

# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)
# B14 = B반의 14번 학생 이렇게 만들 수 있을 것이다.

Classes = namedtuple('Classes', ['rank','number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split() #이렇게하면 공백기준 리스트생성됨

print(numbers)
print(ranks)

# list comprehension 
students = [Classes(rank,number) for rank in ranks for number in numbers]

print(len(students))
print(students)
# 데이터가 딱딱관리가된다. 

# 사실 list comprehension 보다 아래를 추천한다.
# 이는 위의 numbers와 rank 선언없이 사용할 수 있다.
# 아래처럼 위의 내용을 띄어쓰기, 들여쓰기를 줘서 students2에 넣는다.
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(len(students2))
print(students)

# 출력 
for s in students2:
    print(s)
    
# NamedTuple은 가공하려는 데이터를
# 데이터 타입형태로 사용할 수 있다는 것이다.
# 이 네임드튜플형태를 원하는대로 딕셔너리 형태로, json 형태로 변환해서 사용할 수 있다.
# 다음시간에 시퀀스를 다뤄보도록 하겠다.
