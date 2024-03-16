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
# 3. 가변(List, bytearray, array.array, memoryview, deque)
# 4. 불변(tuple, str, bytes)

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


