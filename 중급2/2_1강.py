# 첫번째 파일을 만들고 문법수업을 진행하겠다.
# 파이썬 고급은 알아야 개발자를 위해서는 필수 문법이다.
# 데이터 사이언티스트, 웹, IoT, 빅데이터 하둡 등 어떤 분야에 있던
# 파이썬코드를 같이 사용할 수 있다.
# 파이썬 고유의 기능을 알아야 오픈 소스라던지, 정교한 프로그래밍을 할 수 있다.
# 똑같은 사양으로 성능 집약적으로 읽기 좋은, 성능 좋은 코드가 나올 수 있다.

# Variable scope
# 여러 타 프로그래밍언어 또한 scope를 가지고 있다.

"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals       
"""
"""
전역변수는 주로 변하지 않는 고정 값에 사용
지역변수 사용 이유 : 지역변수는 함수 내의 로직 해결에 국한, 소멸주기(함수 실행 해제 시 소멸)
전역변수를 지역내에서 수정되는 것은 권장되지 않는다.
"""
# 전역변수
# 지역변수
# ex1
a = 10 # Global variable

def foo() :
    # Read global variable
    print('Ex1 > ', a)
    
foo()

# Read global variable
print('Ex1 > ',a)

# Ex2
b = 20
# 파이썬은 함수 내 b를 찾고 없으면 밖에서 찾는다.
def bar() :
    b = 30 # Local variable
    print('Ex2 > ', b) # Read local variable
    
bar()
print('Ex2 >', b) # 글로벌에서 있으므로 가져옴, 없으면 예외발생


# Ex3
c = 40

def foobar() :
    # c = c + 10 # 이렇게만 하면 unboundLocalError 가남.
    # c = 10, c+= 100 이 3개다 에러 발생함   
    print('Ex3 >', c)

foobar() 

# Ex4
d = 50
def foobar() :
    # c = c + 10 # 이렇게만 하면 unbound 참조 에러가남.
    # 아래처럼 하면 전역 scope를 읽을 수 있을 뿐아니라 쓰기도 가능하게 만듦
    # 그러나 global 사용을 자제하자는 의견이 있다. 
    global d 
    d = 60
    d += 100
    print('Ex4 >', d)

foobar() 


# Ex5(중요)
# locals() # 지역 전체 출력
# 코딩테스트에서 인용되는 경우도 있었음.
def outer () : # local 1
    e = 70
    # 아래패턴은 클로저 패턴 또는 데코레이터를 만들때 이 패턴을 사용한다.
    def inner() : # local 2
        nonlocal e
        e += 10 # e = e+10
        print('Ex5 > ', e)
    return inner 

# 과연 local 1과 local 2가 공유가 될 것인가?
# 공유가 안된다. local 안에 local 변수가 존재할 경우 상위 지역변수의 값을 수정할 떄는
# nonlocal e 라는 예약어를 넣어야 된다.
# 이렇게 하나의 변수를 여러번 global 함수없이 재사용하기 위해 클로저를 사용한다.
# 요약)클로저 = 함수쨰로 이 변수 박제, 여기의 경우 10을 더해주고 박제이므로 실행할떄마다 10씩 상승됨.
in_test = outer() # Closure

in_test()
in_test()
in_test()
in_test()

# Ex6

def func(var):
    x = 10
    def printer() :
        print('Ex6 > ', "printer Func Inner")
    print('func Inner', locals())

# var 매개변수가 지역변수로 hi도 출력되고 x도 출력됬다.(locals()에 의해)
# print라는 함수도 가지고 있으므로 function func 도 출력되고

func('Hi')

# Ex7
# Globals() 전역 전체 출력
# 지금까지 했던 선언했던 모든 값들이 전부 출력을 해주게 된다.
# a = 100 이라고 선언하는 순간 
# globals()['a'] = 100 으로 선언하는 것과 같다.

print('Ex 7 >',globals())


# Ex8(지역 -> 전역 변수 생성)
# 변수를 대량으로 만들 때
for i in range(1,10) :
    for k in range(1,10):
        globals()['plus_{}_{}'.format(i,k)] = i+k
      
print(globals()) # 구구단으로 이루어진 값을 동적으로 할당 가능
#print(plus_5_5) # 10 출력됨
  
