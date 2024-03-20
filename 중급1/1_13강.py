# 데코레이터는 꾸미는 장식
# 데코레이터의 본질은 클로저이다.
# 말로설명하긴어려우므로 데코레이터를 사용하고 안하고의 차이를 예제로 보겠다.

# 데코레이터(Decorator)
# 데코레이터를 작성하는 것은 간단하지 않으며 다음과 같은 내용을 이해해야한다.
# 1) 클로저
# 2) 함수를 일급 인자로 활용하는 법
# 3) 가변인자
# 4) 인자풀기(언팩킹)
# 5) 파이썬이 소스코드를 불러오는 자세한 과정

# 데코레이터를 사용할 때 장점들이 있다.
# 장점 : 
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크 ,유효성 체크 -> 공통 기능
# -> 예로 100가지 함수에 대한 시작/ 실행시간을 측정을 해주는 코드가 있다면
# 이 측정하는 코드를 100가지 함수에 데코해주면 된다.
# -> 텐서플로우, 딥러닝 등 다 데코레이터가 붙어있다.
# 3. 조합해서 사용 용이

# 단점 :
# 1. 가독성 감소..? // 데코레이션이 너무 많아지면 추적 복잡
# 2. 특정 기능에 한정된 함수 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
# 어떤 사람이 웹에서 이 메뉴에서 1~5분 정도 머물더라, 이 웹에서 메뉴를 많이클릭한다더라 와같이
# 데코레이터로 한번만 만들어놓음 통계로 작성이 가능해진다.

import time
# 클로저 작성 방법
# 1) 기본적인 클로저의 형태 구성
# def perf_clock (func) : 
#    def perf_clocked(*args) :
#        return result
#    return perf_clocked

# 2) 함수 시작시간 작성
# 기본적인 클로저의 형태 -> 데코레이터로 활용 가능
def perf_clock (func) :  # 실행되는 함수가 계속 바뀌더라도 result에서 결과를 받는다.
    def perf_clocked(*args) : # arg 함수는 내부에서 패킹해서받고 
        # 함수 시작시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args) 
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행함수 명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과출력
        print('[%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))
        return result
    return perf_clocked



# time_func이 per_clock이 func로 넘어와서 실행이 되므로 공통적으로 생성되는 로그성 변수를 데코해줄 수 있다.
# 여러가지 구현하고싶은 함수 구현
def time_func(seconds) :
    time.sleep(seconds)
    

def sum_func(*numbers) :
    return sum(numbers)


# 데코레이터 미사용일때
none_deco1 = perf_clock(time_func) 
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)
print('-'*40 ,'Called NoneDecorator -> time_func')
print()
none_deco1(1.5) # 밖의 함수(perf_clock)를 받아서 안의 함수(none_deco1)를 실행해야되는 단점이 있다.
print('-'*40 ,'Called NoneDecorator -> sum_func')
print()
none_deco2(100, 200, 300, 400)

# 데코레이터를 사용
# 위의 밖의, 안의 함수에 대한 사용없이 실행이 된다.

@perf_clock 
def time_func(seconds) :
    time.sleep(seconds)
    
@perf_clock
def sum_func(*numbers) :
    return sum(numbers)

# 이경우 원함수로 바로 실행이가능하다.
print('-'*40 ,'Called Decorator -> time_func')
print()
time_func(1.5)
print('-'*40 ,'Called Decorator -> time_func')
print()
sum_func(100,200,300,400,500)

# 대부분이 데코레이터로 되어있다.
# 사용측면에서 데코레이터가 훨씬 빠르다는 것을 알 수 있다.
# 여기까지하고 이해가안된 부분들 복습하는걸 추천한다.