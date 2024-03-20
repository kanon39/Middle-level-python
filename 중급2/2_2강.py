# 대량의 데이터를 처리할 때 시퀀스 형 데이터를 다룰 때
# 분야에 상관 없이 핸들링을 하기 떄문에 많이 사용한다.
# 반복된 for문으로 처리를 할때는 데이터가적을떈 괜찮으나 
# 데이터가 많을 경우에는 Lambda, reduce, map, filter로도 빠른 연산 구현이 가능하다.

"""
Chapter1 Advancer(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lambda, map, filter, reduce
"""
"""
lambda 장점 : 
1. 익명, 모든 프로그래밍과 같이 힙 영역에서 사용 즉시 소멸됨.
2. 파이썬 다운 코드, 파이썬 가비지 컬렉션(Count=0)
3. 일반함수와는 다르게 재사용성을 위해 메모리에 저장 안됨.

일반 함수 : 재사용성 위해 메모리에 저장함.
(중요)시퀀스형 전처리에 Reduce, Map, filter 주로 사용함.
내부적으로 iterable한 값을 리턴하기 때문에 한번에 메모리에 올리지 않고
그떄 그때 콜을 할 때 부를 수 있어서 메모리 낭비를 줄일 수 있다.

"""
# Ex1
cul = lambda a, b, c : a*b+c
print('Ex >', cul(10,15,20))

# Map 함수는 수행된 시퀀스에서 iterable하게 하나씩 뺴온다.
digits1 = [x*10 for x in range(1,11)] 
print(digits1)

# map은 두개의인자를 받는다. 첫번쨰는 함수, 두번째는 시퀀스를 받는다.
result = map(lambda x : x**2, digits1)
print(result) # 이결과 map object가 실행이된다.

# 결과 확인을 위해 형 변환을 해보면
result1 = list(map(lambda x : x**2, digits1))
print(result1) # 이결과 map object가 실행이된다.

# 만약에 lambda가 없다면 아래처럼 사용 해야 됨
# 들어가있는 인자에 시퀀스이기 때문에 iterable하게 각 값이 제곱이 되어 리턴됨.
def ex2_func(x) :
    return x ** 2

# 오픈 소스라던지 많이 구현된 코드들을 보면 아래처럼도 구현이 되어 있다.
# 아래 부분만 패키지화해서 호출해서 쓰면 기능별로 모듈화해서 실행할 수 있다.
def also_square(nums) :
    def double(x):
        return x ** 2
    return map(double, nums)

print('Ex2 > ', list(also_square(digits1)))

# Ex3
# filter 함수 :
#  - 첫번째 인수에 True, False 결과가 나오게코드를 짜야됨.
#  - 두번째 인수에 필터할 시퀀스가 들어감.
digits2 = [x for x in range(1,11)]

result = list(filter(lambda x : x % 2 ==0, digits2))

print('Ex3 > ', result)

def also_evens(nums) :
    def is_even(x) :
        return x % 2 == 0
    return filter(is_even, nums)

print('Ex3 > ', list(also_evens(digits2)))

# reduce 는 누적으로 합계를 구할 때 사용한다.
# 만약 데이터의 이메일에서 데이터에서 여러개를 참조해서 보낼때
# reduce로 뽑아낼 수 있다. python 3.0 이상부터 import를 해서 사용하게 바뀜

from functools import reduce

digits3 = [x for x in range(1,101)]

result = reduce(lambda x, y : x+y, digits3) # reduce에서 저정해둔 함수의 return값으로 나옴
print('Ex4 > ', result)

def also_add(nums) :
    def add_plus(x,y):
        return x+y
    return reduce(add_plus,nums)
print('Ex4 > ', also_add(digits3))

