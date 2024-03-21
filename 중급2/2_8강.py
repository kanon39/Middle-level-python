# JAVA와 같은 다른 프로그래밍 언어에서도 많이 쓰임
# Method overriding

"""
Chapter 2
Python Advanced(2) - Method Overriding
Keyword - Overriding, OOP, 다형성

"""

"""
메소드 오버라딩 효과
1. 서브 클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용 가능
3. 부모 클래스의 메소드를 추상화 후 사용가능(구조적 접근이 가능)
4. 확장 가능, 다형성(다양한 방식으로 동작, 부모를 하나 만들고 자식마다 다르게 쓰임)
5. 가독성 증가, 오류 가능성 감소, 메소드 이름 절약, 유지보수성 증가 등

"""
# Ex1 
# 기본 Overriding 예제

class ParentEx1() :
    def __init__(self) :
        self.value = 5
        
    def get_value(self) :
        return self.value

class ChildEx1(ParentEx1) : #부모 클래스에서 상속
    pass

c1 = ChildEx1()
p1 = ParentEx1()

# 부모 클래스 메소드 호출
print('Ex1 > ', c1.get_value())

# c1의 모든 속성을 출력
print('Ex1 > ', dir(c1)) # 자식에 부모의 함수들과 변수가 들어감확인가능

# 부모 & 자식 모든 속성 출력
print('Ex1 >', dir(ChildEx1))
print('Ex1 >', dir(ParentEx1))

print()
#  인스턴스 되기전 클래스의 네임스페이스 영역을 보자.
# 부모 네임스페이스에는 다 있으나
print('Ex > ', ParentEx1.__dict__)
# 자식의 네임스페이스에는 부모와 다르게 없음.
# 인스턴스가 되는 시점에 자식에 담기는 것이디 떄문임.
print('Ex > ', ChildEx1.__dict__) 

# Ex2 
# 기본 Overriding 메소드 재정의
# 부모에서 만들어논 메소드를 자식에서 재정의한다.

class ParentEx2() :
    def __init__(self) :
        self.value = 5
        
    def get_value(self) :
        return self.value

class ChildEx2(ParentEx2) :
    def get_value(self) :
        return self.value * 10 #부모에서 value 가져와서 10곱해줌

c2 = ChildEx2()

# 자식 메소드 재정의 후 호출
print('Ex2 >', c2.get_value())


# Ex3
# 실제로 실무에서 많이 사용해 볼만한 예제이다.
# overriding 다형성 예제

import datetime

class Logger(object) :
    def log(self, msg) :
        print(msg)
        
class TimestampLogger(Logger) :
    def log (self, msg) :
        message = "{ts} {msg}".format(ts = datetime.datetime.now(), msg=msg)
        # 부모로 부터 print를 호출한다하면 부모 class와 self인자를 넣어준다.
        # super().log(message)
        # 위는 아래를 더 간략히 표현한 것이다.위와 아래가 같음.
        # 아래가 더 정확함.
        super(TimestampLogger, self).log(message)
        
class DateLogger(Logger) :
    def log (self, msg) :
        message = "{ts} {msg}".format(ts = datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

# 우리 가족은 log 라는 메소드를 써, 이게 정확하니까.
# 어떤 자식은 시분초를,
# 어떤 자식은 데이트를 맡는다.

# 메소드 재정의 실습
# 아래에서 None이 나오는 이유는 print문안에 또다른 print문이 있기 때문
print('Ex3 > ', l.log('Called logger.'))
print('Ex3 > ', t.log('Called timestamp logger.'))
print('Ex3 > ', d.log('Called date logger.'))
print()
print()
# 따라서 아래처럼 해도 출력됨
l.log('test1')
t.log('test2')
d.log('test3')

