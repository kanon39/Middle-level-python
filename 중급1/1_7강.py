# 파이썬 시퀀스
# 시퀀스는 순서가 있는, 나열된 자료를 의미하며 대표 종류 중 하나로 리스트가 있다.
# 시퀀스는 일렬로 나열되어 있는데 번호가 붙은 걸로 알 수 있다.

# 파이썬에서는 데이터 종류가 두개로 나뉜다.
# 1. 컨테이너형태의 자료(Container : 트럭에 컨테이너를 싣고가는것 처럼 컨테이너 안에 여러가지를 실을 수 있다.)
# : 서로 다른 자료형[List, tuple, collections.deque]을 저장할 수 있다.
# 예시
# a = [3, 3.0, 'a']
# print(a)

# 2. 플랫(Flat : )
# : 한개의 자료형[str, bytes, bytearray, array.array, memoryview]만 담을 수 있다.
# bytearray등은 사용을 안할 뿐이지 데이터 분석이나 대용량 처리를 할 때 사용할 때가 온다.
# 조금이라도 빠르게, 메모리를 더 잘 활용을 하고 싶다 할 때 활용된다.
# 그렇기에 자연어처리나, 숫자 등의 숫자형만으로 구성되어 있을때 플랫을 쓴다.

# 경력시험, 코딩테스트 등 시험을 칠때 적절한 자료형을 찾는 것도 중요하다.
# - 가변(List, bytearray, array.array, memoryview, deque)
# - 불변(tuple, str, bytes)

# 이 4가지를 잘 이해한다면 파이썬 고급에 한걸음 더 다가갈 것이다.

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists) 
chars = '+_)(**&^%#@!)'
# 위의 chars에 h를 대입하면 에러가 발생한다.
# chars[2] = 'h'

# 이를 리스트에 담아보겠다.
# 보기에는 하나의 문자열로 보이지만 하나하나가 인덱스가 있다.

code_list1 = []

# ord는 각 문자열에 해당하는 유니코드를 출력해준다.
# 리스트로 하나하나 유니코드를 살펴보겠다.
for s in chars :
    # 유니코드  리스트
    code_list1.append(ord(s))

print(code_list1)
# 위의 for 문에서 append 쓰는 것보다 아래처럼 comprehending 쓰는 것이
# 좀 더 좋지만 큰 차이는 없다. 데이가 많아지면 아래처럼 쓰는걸 가이드에서는
# 추천하고 있다.

# 지능형 리스트(Comprehending Lists) 
code_list2 = [ord(s) for s in chars]

print(code_list2)

# comprehending Lists + Map, Filter
# 유니코드가 40 이상인 문자열을 가져와 보겠다.

code_list3 = [ord(s) for s in chars if ord(s) >40]
# 많이 쓰이진 않겠지만 필터 함수와 map 함수를 써서 다시 표현해보겠다.
# list()로 컴버팅이 들어가고 
# filter 함수는 두개의 인자를 받는다 첫번째는 익명함수나 또는 함수를 받고 두번째는 리스트나 자료구조를 받는다.
# 여기서는 lambda 함수를 받겠다.
# lambda 함수는 x하나를 받아서 얘가 40보다 큰지 True, False로 리턴해주면 되고
# 다음 인자로 chars로 들어가도 되지만 지금은 문자열 형태로 되어 있기 때문에
# 얘를 유니코드로 바꿔주는함수인 ord로 매핑한다하면 map 함수로 서로 반복을 해줘야 된다.
# 따라서 map 함수 내에 ord 함수를 chars 갯수만큼 넣어줘 라는 의미로 map(ord, chars)를 넣는다.
# 그러면 map 함수 결과 [43, 95, 41, 40, 42, 42, 38, 94, 37, 35, 64, 33, 41]가 나오게되고
# 43부터 하나하나 40보다 커? True야? 라고해서 True인 것들만 리스트로 반환한다.

code_list4 = list(filter(lambda x : x>40, map(ord, chars)))

# 위와 같이 데이터 전처리를 할 때 filter 함수를 자주쓴다.

print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

# 이번엔 반대로 유니코드를 문자로 반환해 보겠다.
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# Generator(제네레이터)에 대해서 학습을하겠다.
# 제네레이터는 매우매우 중요하다.
# 파이썬에서는 다른 언어의 array를 파이썬에서는 list로 사용하는 구나 싶지만
# 파이썬에서도 import array를 따로 사용할 수 있다.
# array는 플랫이며 가변형이다.

# 제네리이터는 시퀀스 결과를 만들어 내고
# (매우중요)작동하는데 로컬 상태를 유지하고 다음번에 내가 반환할 값의 위치를 정확히 가지고 있다는 뜻입니다.
# 그래서 Generator(제네레이터)는 파워풀한 iterater(이터레이터)이다.
# __iter__ 라는 얘가 dir 속성에 있으면
# 이 데이터속성은 연속적인 for문 등에서 반환(순회)가ㅣ가능하다라는 뜻이다.
# 그래서 제너레이터는 작은 메모리 조각으로도 계속 연속되는 데이터를 만들어 낸다는 것이다.
# 만약 a라는 데이터가 1부터 1억까지 값들을 포함하게된다면 많은 메모리를 차지하게 될 것이다.
# 많은 메모리를 차지한다면 그만큼 엑세스(읽고수정하고 등)를 해서 계산하는데
# 비효율 적이기 때문에 제너레이터를 사용한다.
# 제너레이터는 다음에 내가 반환할 값만 가지고 있다면, 즉 
# 1을 반환하고 2를 반환할 위치정보만 가지고 있다면 메모리 사용량은 극히 적을 것이다.
# 따라서 제너레이터는 연속되는 값을 만들어내는데 메모리 사용량을 쉽게 사용할 수 있다.
# 파이썬 제너레이터 장점 구글에 검색하면 좋은 참고가 될 것이다.
# 요약 : generator : 한번에 한 개의 항목을 생성(메모리 유지x)

# 파이썬 제너레이터를 이용해서 array를 활용해 보겠다.

import array 


# 아래처럼 list comprehention을 사용하면 값을 만들어 버린다.
tuple_g = [ord(s) for s in chars]
# 출력 결과 : [43, 95, 41, 40, 42, 42, 38, 94, 37, 35, 64, 33, 41]
# 하지만 아래처럼 []를 ()로 바꿔주면 
tuple_g = (ord(s) for s in chars)
# 출력 결과 : <generator object <genexpr> at 0x0000015932E313C0> 라고 나온다.
# 아직 위위와 같이 값을 생성하기 전이고 첫번째 값인 43을 반환할 준비만 한 상태 입니다.
# 부릉부릉(제너레이터는 발전기란뜻이므로..) 준비중..
print(tuple_g)

# type으로 제너레이터 형태임을 알 수 있다.
print(type(tuple_g))

# next를 출력하면 실제 값이 나온다.
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

# 이제 array로 만들어 보겠다.
# array는 list보다 더욱 더 low-level에서 numpy의 ndarray
# 등 수치연산에 최적화 되어 있다.

array_g = array.array('I',(ord(s) for s in chars))
print(array_g)
print(type(array_g))
# array를 list로 반환해주는 tolist()
print(array_g.tolist())

print()
print()

# 제네레이터 예제
# 지난 시간에 했던 A,B,C,D 반에 20명씩을 제네레이터로 만들어 보겠다.
# '%s'로 문자열이다라고 알려준다.
# c 문자로 매핑해주고
# 문자열로 바꿔주니까 n에 대한 형변환으로 str()을 해준다.
print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))
# 위의 경우 제네레이터로 출력이 되기 때문에 값을 볼 수 없다.
# 즉흥적으로 값을보기 위해서는 아래처럼 코드를 쓴다.
# 전체 한꺼번에 값 출력이 아니라 하나하나 값을 출력한다.
for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)
    
# 리스트 쓸때 주의할 점 (반드시알고있어야 실수를 안함)
# 깊은 복사, 얕은 복사에 대한 이해가 필요

# marks1리스트에 곱하기 3를해서 4번 반복이 되게하자.
# 반복은 하는데 사용을 안할때는 여러 문자가 들어가도되나 일반적으로 언더바(_)를 입력해준다.
marks1 = [['~'] *3 for _ in range(4)]
# 또 굳이 for 안쓰고 아래처럼 만들수도 있다
marks2 = [['~']*3]*4

# 하지만 크리티컬한 문제점이 있다.
# 첫번째 리스트에서 거기의 index1 번이므로 수정을 한다 하면
# 첫번째 리스트 내 두번째 원소값이 대문자 X가 들어가게 된다.
marks1[0][1] = 'x'
print(marks1)
print()
print()
# 그런데 이를 marks2에 수정하면 모든 리스트의 첫번째가 다 바뀌게된다.
marks2[0][1] = 'x'
print(marks2)

# 이렇게 되면 의도하지 않은 결과값이 수정되는 큰 문제가 발생할 수 있다.
# 이일이 발생한 이유는 marks1의 경우 첫번째 값이 정확히 복사가 되었기 때문에
# 각 ['~','~','~']별로 ID(메모리 주소)값이 다른 것이고
# marks1의 경우 하나의 ID(메모리 주소)값이 복사가 된 것이기 때문에 
# 수정이 이루어진 것이다.
# 따라서 ID값을 출력하면 증명이 가능하다.
# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2]) 

# 즉 marks2와 같이 리스트를 만들고 곱해주는 카피형인 참조형 구조체를 다룰 때는 조심해야 된다.
# ID 값을 찍어보자. 급하게 말고 천천히 개발해보면 실수를 줄일 수 있다.


# 이후는 리스트 및 튜플 외 다른 것들에 대해 배워보겠다.
