# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
# -> 잠깐 공부하다가 멈추고 밥먹고 다시돌아와서 공부하는 것
# -> 내가 어디까지 했는지 알아야 함(클로저)
# -> 단일 프로그램안에서 여러 일을 쉽게 해결할 때 씀
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행
# -> 여러 프로세스나 워커가 동시에 수행
# -> CPU는 하나지만 여러일을 동시에 해내는 코루틴 등이 있다.
# -> 속도

# 병렬성도 병행성도 둘 다 지원한다.
# Generator Ex1

# 단일 프로그램 -> 여기선 단일 함수
def generator_ex1() :
    print('Start')   # ------ 1차실행 ------
    yield 'A Point'  # ---------------------ex.네이버에서 크롤링 
    print('Continue') # ======= 2차 실행========
    yield 'B Point' # ==========================ex. 구글에서 크롤링
    print('End') # 여기서 끝
    
# yield가 포함되어 제너레이터 함수이므로 iter함수 호출가능
# yield는 어디까지 했는지를 알고있다->이게 제일중요
# yield는 return의 역할을 한다고 볼 수 있음.
temp = iter(generator_ex1())

#print(next(temp))
#print(next(temp))
#print(next(temp))

# 여러 일을 동시에 실행하는 메커니즘이다.
#for v in generator_ex1() :
#    print(v)

# Genrator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1()) # 제너레이터 형태

#print(temp2)
#print(temp3)
for i in temp2 : 
    print(i)
    
# yield가 리턴의 역할을 하기 때문에 A Point 반복이 완료되면
# B Point에 대한 반복이 진행된다.
for i in temp3 : 
    print(i)

print()
print()


# Generator Ex3 (중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby ...
# 이를 알면 데이터를 센스 있게 만들 수있다.

# 첫번째로 데이터를 무한대로 만들고 싶다
# itertools가 많이 유용할 때가 많다
import itertools
# 1부터 계속 2.5 계속 더해주기
gen1 = itertools.count(1,2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한
# 계속 2.5가 1에서 무한으로 더해지게 됨


# 조건
# 1부터 2.5까지 계속 증가하는데  1000 미만까지 값 생성
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1,2.5))
#for v in gen2 :
#    print(v)

print()

# 필터의 반대 역할
gen3 = itertools.filterfalse(lambda n: n<3, [1,2,3,4,5])
# 3미만인 값 제외한 3,4,5가 결과로 나옴
for v in gen3 :
    print(v)
print()

# 누적합계
gen4 = itertools.accumulate([x for x in range(1,101)])
#for v in gen4 :
#    print(v)

# 연결1
# chain도 개발에서 중요하다.
# 서로 다른 iterable이라고해서 chain 가능
# 브로드케스트라고 해서 사칙연산으로도 연결 가능
gen5 = itertools.chain('ABCDE', range(1,11,2))
print(list(gen5))

# 연결2
# 튜플형 리스트로 출력을 해준다.
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7)) # 이터레티브한 값을 개별로 쪼개기

# 개별
# repeat은 개별로 모든 조합의 경우의 수가 나오게 된다.
# repeat = 2라면 조합이 2개인 모든 경우의 수를 저장한다.
gen8 = itertools.product('ABCDE', repeat = 2) 
print(list(gen7)) # 이터레티브한 값을 개별로 쪼개기

# 그룹화
# iterative 한 값들을 모아 집계를 낸다.
gen9 = itertools.groupby('AAABBCCCCDDEEE')
#print(list(gen9)) # 무언가 복잡하게 나온다.

for chr, group in gen9 :
    print(chr, ' : ', list(group))

