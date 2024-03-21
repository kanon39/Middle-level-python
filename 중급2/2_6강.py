# 파이썬의 Underscore 

"""
Chapter 2
Python Advanced(2) - Property(1) - Underscore
Keyword - access modifier(접근지정자), underscore

"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
"""

# Ex1
# underscore (_)

# 1. 인터프리터에서 사용 (그닥안중요)
# 2. 값을 무시
# 3. 네이밍(구체화, 자릿수)

# unpacking
x, _, y = (1,2,3)
# 언패킹때 2는 무시됨.
print(x,y)
# 아래는 2,3,4가 날아가고 처음값과 끝값만 남음
a, *_, b = (1,2,3,4,5)
print(a,b)
print('Ex > ', x,y, a, b)


# for 패턴에서 값을 무시할때 씀
for _ in range(10) :
    pass

# 아래패턴 많이 씀
# 값만 출력하겠고 index는 무시하겠다 라는의미
for _, val in enumerate(range(10)) :
    pass

# Ex2
# 접근 지정자
# 파이썬에서 Public 은 강제가 아니다, 약속된 규약에 따라 코딩을 장려함(자유도, 책임감 장려).
# 그러나 타 클래스의 변수, 인스턴스 변수 값 쓰기 장려 안함 -> Naming Mangling 검색 해보기
# 아래가 약속된 규약
# name : 그냥 변수 이름을 지정하면 public 이된다.
# _name : protected (상속관계에서변수를 나타낼때 쓴다.)
# __name : private 숨겨져있음(캡슐화) -> 이 변수는 건들지말아주세요 란 뜻

# 타 클래스에서 언더바 두개(__)는 접근하지않는 것이 원칙. 

# No use Proprety

class SampleA :
    def __init__(self) :
        self.x = 0 # 얘는 값 바꿔도되겠군
        self.__y = 0 # 얘는 건들지마시오
        self._z = 0 # 얘는 하위 클래스에서 이용할 꺼야
        
a = SampleA()
a.x = 1 # ORM, 클래스랑 데이터베이스랑 1:1로 매핑하는 등 특이한 상황아니면
# 직접접근해서 변경하는건 어떤 프로그래밍언어도 권장되지 않음.

print('Ex 2  > x : {}'.format(a.x))

# 아래와 같이 언다바 두개가 있으면 출력이 되지 않는 것을 알 수 있다.
#print('Ex 2  > y : {}'.format(a.__y))

print('Ex 2  > z : {}'.format(a._z))

# dir로 획인하면 __y를 임의대로 _SampleA__y 로 바꾸었다.
print('Ex 2 > ', dir(a))

# 만약 집요하게 바꾸면 바뀐다. 즉 못하게는 안되게 안막아놨음.
# 변수 접근 후 수정 부분에서 일관성 및 가속성이 하락됨.
a._SampleA__y = 2 # 수정 가능
print('Ex 2  > y : {}'.format(a._SampleA__y))


# Ex3
# 메소드 활용 Getter, Setter 추후 배울 예정

class SampleB :
    def __init__(self) :
        self.x = 0
        self.__y = 0 # _SampleB__y 로 바뀌게됨
    
    # 아래처럼 get_y외 set_y함수로 캡슐화하여 작성하면 
    # _SampleB__y 로 직접접근 안해도 됨.
    def get_y(self) :
        return self.__y
    
    def set_y(self, value) :
        self.__y = value

b = SampleB()
b.x = 1
b.set_y(2)

print('Ex3 > x : {}'.format(b.x))
print('Ex3 > y : {}'.format(b.get_y()))

# 이렇게 계속 코딩하는 습관을 들이자.
