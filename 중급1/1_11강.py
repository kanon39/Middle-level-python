# 파이썬 일급함수(객체)
# 이번과정 굉장히 중요

# 파이썬 일급함수를 활용하여 함수형 프로그래밍이 가능하다.
# 나중에 시간이 된다면 함수형 파이썬 프로그래밍 책을 찾아 읽어보는 것도 좋다.

# 함수형 프로그래밍은 코드간결 작성으로 개발시간 단축, 
# 순수함수(Pure function)을 지향하여 동시에 여러 스레드에서 문제없이 동작하는 프로그램을 말한다.
# 스레드가 나오면 주니어보다는 시니어 쪽이며 어느정도 프로그래밍이 익숙할때, 또 함수형을 완전히 이해했을 때 
# 효율이 굉장히 상승하게되는 프로그래밍 방법이다.

# 이를 가능하게 해주는 First class 일급함수이다.
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화(실행시점 초기화)
# 2. 변수 할당 가능
# 3. 함수를 다른 파라미터인수 전달 가능
# 4. 함수 결과 반환 가능(return)


# 5! = 5*4*3*2*1 5팩토리얼은 이와 같이 쓸 수 있다.
# 이를 함수로 만들어 보겠다.

def factorial(n) :
    '''
    Factorial Function -> n : int
    '''
    if n == 1: # n<2
        return 1
    return n*factorial(n-1) # 함수내에 동일 함수 호출하는 재귀함수이다.
    # n이 2보다 작을때는 1을 반환하고
    # 2보다 크거나작을 경우 계속 자기 함수를호출한다.
    
#  위의 함수를 객체취급을 하는지 증명을 해보겠다.

class A :
    pass
    

# 만들어논 함수를 호출해보자
print(factorial(5))
print(factorial.__doc__)
print(type(factorial)) # 함수가 class로 결과가나온다.
print(type(factorial), type(A)) # 클래스도, 함수도 class 타입으로 나온다. 즉 함수도 class의 내부 dir값을 가지고 있다.
# factorial 함수 안에 포함되어 있는 Class문내 dir을 제외하면 함수의 dir값만  남게된다.
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

print(factorial.__name__)
print()
print()
print(factorial.__code__)





# 이렇게 함수는 객체취급을 하는지 알수 있었다.
# 1. 런타임 초기화(실행시점 초기화)
# 2. 변수 할당 가능
# 3. 함수를 다른 파라미터인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 변수 할당
var_func = factorial # 함수 자체 할당
print(var_func)
print(var_func(10)) # 변수에 할당한 상태로 함수 활용가능
print(list(map(var_func, range(1,11)))) # 각각의 팩토리얼값을 리스트로 출력함.

# 함수 인수전달 및 함수로 결과 반환 _> 고위함수(Higher - order function)
# -> 파이썬을 오래공부하면 듣게 될 것이다.
# map, filter, reduce는 반드시 알아야 된다. 프론트 엔드에서도 이 3개 함수가 다 있다.
# 5 팩토리얼 값을 i를 2로나누었을때 홀수값일경우 출력하는 로직
# 코드를 작성하는 것도 중요하지만 함수를 익명함수 lambda를 이용하여 filter의 인수로 전달됐다는 것이다.
print(list(map(var_func, filter(lambda x: x %2, range(1,6)))))

# 위 print 문은 좀 복잡하다. 두 결과는 모두 같으나 가독성 면에서는 아래가 더 좋다.
print([var_func(i) for i in range(1,6) if i % 2]) 

print()
print()

# 리듀스 함수 다뤄보기
from functools import reduce  # 따로 임포트 해야한다.
from operator import add # 더해주는 함수-> + 와 같다.

# 1부터 10까지의 합을 구하려고하자.
print(sum(range(1,11))) # range를 하면 리스트가 아웃풋이나오고 이를 sum을한다.

# 나는 더해줄 건데(add), 어떤 걸 누적합을 할까? (range)
print(reduce(add, range(1,11)))

# 보통 코드를 짜라고하면 sum을 짜는게 맞다. 누적할때 쓰는함수가 reduce이다.

# 익명 함수 배우기(lambda)
# 전문가를 위한 파이썬 발췌하자면, 가급적 주석을 꼭 작성해둬라.
# 가급적 익명함수 보다는 함수를 작성해라 라고 권장하고 있다.
# 일반 함수 형태로 리팩토링 권장.

# 두개 인자(t,x)를 받아서 x+t를 반환해보겠다.
print(reduce(lambda x, t : x+t, range(1,11)))

print()
print()

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출가능 확인
# __call__이라는 에튜리뷰트가 있으면 함수로써의 호출이 가능하다는것이다. 
# 있기때문에 print(var_func(10))을 위에서 호출해 보았다.

print(callable(str)) # 이는 호출이 가능한 상태로 True라고 출력이된다.
str('a') # 이라고할때정상적으로 호출이 되는 걸 볼 수 있다.

# 그렇다면 위에서만든 class A 또한 호출이가능할까?
print(callable(str), callable(A)) # 둘다 True로 호출이가능하다고 나온다.
print(callable(str), callable(A), callable(list), callable(3.14)) # 3.14는 상수이므로 호출이불가하다.
# 예로 3.14()는 불가능하다.
# 에러 메시지로 float object is not callable < 즉 함수가 아니라는 뜻이다.

# partial 사용법 : 진짜 중요 많이 사용한다.
# 인수 고정하여 콜백 함수 사용할 때 사용한다.
from operator import mul
from functools import partial

# 아래에서 10은 항상 박혀있고 뒤의 것만 변동이 된다면
print(mul(10,10))

# 인수 고정, 일급객체이므로 첫번째 인수는 함수가 들어가고 그다음 5를 넣는다.
# 그 다음 일급객체이므로 five라는 인수에 함수를 할당했다. 
# 현 상태는 5 곱하기 ? 이다.
five = partial(mul, 5)
print(five(10)) # 이를 진행하면 50이 나온다.
print(five(100)) # 이를 진행하면 500이 나온다.

# 고정 추가
six = partial(five, 6)
# print(six(10)) # 이경우 에러발생. 인자가 이미 five, 6인데, 10까지 받아서 에러발생한다.
# 내가 다 고정해놨으니 호출해서 써 가 parital 함수이다.
# 마지막으로 list comprehention 을 해보겠다.

print([five(i) for i in range(1,11)]) # 5의 배수를 만들 수 있게된다.
print(list(map(five, range(1,11)))) # 동일하게 5의 배수가만들어진다.

# 정리하자면 일급 객체는 함수형 프로그래밍을 가능하게 해주고,
# 함수형 프로그래밍은 코딩할 때 반드시 관심을 가지는것이 좋다.
