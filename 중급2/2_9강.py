# Method overloading

# 오버라이딩은 부모 class 끼리 관련이있고
# 오버로딩은 메소드끼리 관련이 있고
# 파라미터 기반과 관련이 있다.

"""
Chapter 2
Python Advanced(2) - Method Overloading
Keyword - Overloading, OOP, multiple dispatch
"""

"""
메소드 오버로딩 효과
1. 동일 메소드 재정의
2. 네이밍 기능 예측
3. 코드절약, 가독성 향상
4. 메소드파라미터 기반 호출 방식

"""

# Ex1
# 동일 이름 메소드 사용 예제

# 동적 타입 검사는 면접기출문제로도 자주 출제됨.
# 동적 타입 검사 -> 파이썬, 자바, 루비 등은 동적 타입 에러가 실행시에 발견된다.

class SampleA () :
    # 메소드 파라미터 기반 호출 방식이란
    # 파라미터 갯수별로 알맞는 함수가 호출되게 하고싶다하자.
    # 그러나 아래처럼 같은이름의 함수가 있을 경우 아래 add 함수가 위의 add함수를 덮어써버린다.
    # python에서는 이렇게 method 오버로딩을 지원하지 않기 때문
    # 이를 지원하게  만드는게 multiple dispatch다.
    def add(self, x, y) :
        return x + y
    
    def add(self, x, y, z) :
        return x + y+ z
    
    # 패킹으로 해결 가능-> 그러나 우리가 하려는건 오버로딩이므로 주석처리하겠다.
    #def add (self , *args) :
    #    return sum(args)
a = SampleA()

#print('Ex > ', a.add(2,3))

print('Ex1 >', dir(a)) # 들여다보자

# Ex2
# 그럼 과거에 동일이름 메소드 사용을 했을까?
# 자료형에 따른 분기 처리 -> 단일 함수로 여러 가지 기능을 하게해줌.

class SampleB() :
    def add(self, datatype, *args) :
        if datatype == 'int' :
            return sum(args)
        
        if datatype == 'str' :
            return ''.join([x for x in args])
        
b = SampleB()

# 숫자 연산
print('Ex2 > ', b.add('int',5,6))

# 문자 연산
print('Ex2 > ', b.add('str','Hi','Python'))

###  최근에 이런 메소드 오버로딩을 Dispatch를 이용할 수 있게 됬음.

# Ex3
# multipledispatch 패키지를 통한 메소드 오버로딩

from multipledispatch import dispatch

class SampleC ():
    # Ex1 에서 했을떄 예외가 발생한 것을 dispatch를 통해서
    # 실행시킬 수 있다. 이경우 인수 두개받을경우 위에것이,
    # 인수 세개 받을 경우 아랫것이 실행된다.
    # 따라서 함수 이름이 아닌 데이터 타입의 관점에서 메소드 관점에서
    # 가독성 좋은 코딩을 할 수 있게 된다.
    @dispatch(int, int)
    def product(x,y) :
        return x * y
    
    @dispatch(int, int, int)
    def product(x,y,z) :
        return x + y + z
    
    @dispatch(float, float, float)
    def product(x,y,z):
        return x * y * z
    
c = SampleC()

# 정수 파라미터 2개
print('Ex3 > ', c.product(5,6))
# 정수 파라미터 3개
print('Ex3 > ', c.product(5,6,7))
# 실수 파라미터 3개
print('Ex3 > ', c.product(5.0,6.0,7.0))