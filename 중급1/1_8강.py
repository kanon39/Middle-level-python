# 파이썬 시퀀스 실습
# 튜플(Tuple) 고급 사용
# Mutable(가변)
# Immutable(불변)
# Sort vs sorted 실습

# 전세계 개발자들이 만들어논 소스코드를 보면 이해가 안가는 부분들이
# 많을 것이다. 파이썬의 코드의 특징상 문법을 표현하는 방법이 너무나 많기때문.
# 이건 어떻게 코딩을 한거지? 라고 볼 법한 코딩들을 정리해보겠다.

# 1. Tuple Advanced
#  - Unpacking에서 다른 곳에서 나올 법 한 것 봐보겠다.

# 파이썬은 아래의 교차 적용을 쉽게해줄 수 있다.
# b, a = a, b

print(divmod(100, 9)) # 100을 9로 나눴을 때 몫과 나머지를 구해주는 함수
# 튜플로 넣겠다하면 100,9 앞에 아스타(*)를 넣어줘서 인수를 풀어서 실행을 해줘야 한다. => unpacking
# 아스타(*)를 안넣어주면 divmod expected 2 arguments 라는 2개인 인수를 받아야 되는데 지금은 하나다 라는 오류가 출력된다.
print(divmod(*(100,9)))

# 아래의 경우도 실행하면 (11,1)이 아닌 튜플이 풀려서 결과가 나오게 된다.
print(*(divmod(100,9)))

# 위 print 3개가 눈에 익도록 실습하길 권장한다.

# 변수를 선언해서 언패킹에 대해서 깊게 들어가 보겠다. 
# x, y, rest 3개의변수만 두면 range는 0부터 9까지하면 너무 많은 값이 있어 에러가 발생한다.
# 이때 rest앞에*를 붙이면 에러가 발생하지 않게된다.
# 이럴 경우 첫번째 값은 x에, 두번째 값은 y에, 나머지 값은 rest에 싸그라 다 들어가게 된다.
# 데이터를 준비하는 쪽에 하둡 등 활용할 때 이를 많이 활용한다.
x, y, *rest = range(10) 
print(x, y, rest)
# 만약 언팩하는 값이 2개뿐이면 마지막 3번째 변수에 빈 리스트만 들어간다.
x, y, *rest = range(2)
print(x,y,rest)
# 아래의 경우도 3,4,5가 리스트 형태로 rest로 들어간다.
x,y, *rest = 1,2,3,4,5
print(x,y,rest)

print()
print()
print()

# Mutable(가변) vs Immutable(불변)
# 두 가변과 불변형에 대해 ID값을 표시해보고, 연산자를 사용했을 때 어떻게 값을 확인할 수 있는지 확인해보겠다.
# 가변형 list와 불편형인 tuple을 다뤄보겠다.
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l*2 # 두배로 값이 할당됨 (브로드캐스팅)
m = m*2

# 기존 변수명인 l과 m을 재할당하여 id값이 위의 메모리 주소와 달라지게 된다.
print(l, id(l))
print(m, id(m))

# 아래와 같이 실행할 경우 튜플의 경우 불변이기 때문에 생성될 때마다 새로운 메모리주소(아이디)에 l값이  재할당되나
# 리스트의 경우 가변형이기 때문에 같은 메모리주소(아이디)에 m이 재할당된다.
# 따라서 변동이 심한 경우, 이리곱하고 나눠도보고 등등 시도가 많이 필요할 때는 리스트가 적절하다.
# 만약 튜플로 변동이 심한 작업들을 하게되면 계속해서 메모리가 새롭게 할당되기 때문에 용량을 차지하게 되기때문
l *= 2
m *= 2
print(l, id(l))
print(m, id(m))

print()
print()

# 파이썬에서 정렬을 검색하면 sort와 sorted 두개가 나온다.
# 이 두개는 경우에 맞게 잘 사용해야 된다.
# sort, sorted 옵션 : reverse(정렬 반대), key=len(값 길이로 정렬), key=str.lower(소문자로 정렬), key=func... (내가만든함수기준 정렬)

# sorted : 정렬 후 새로운 객체 반환 -> 원본 수정 안됨!!
# sort : 정률 후 객채 직접 반환 -> 원본 직접 수정됨!
# f_list 원본
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon',' strawberry', 'coconut']
# sorted는 원본 반환 안되고 새로운 객체가반환됨
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
# 외부에서 함수만들어도 되나 이럴때 lambda 함수를 씀
# x[-1] 을 쓰면 마지막 글자를 기준으로 정렬됨
print('sorted - ', sorted(f_list, key=lambda x : x[-1]))
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse = True))
# 원본과 비교
print(f_list)

# sort : 정렬 후 객체 직접변경

# 반환 값 확인(None)
# sort를 쓸때는 이 값을 직접 반환할꺼야 라는느낌으로 f_list 점찍고 sort()함수를 적어준다.
# 이경우 f_list.sort()값은 None이 나오는데, 이는 반환할 값이 없기 때문
# f_list를 실행해보면 원본이 직접 변경됨을 알 수 있다.
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(), f_list(reverse=True), f_list)
print('sort -', f_list.sort(), f_list(key=len), f_list)
print('sort -', f_list.sort(), f_list(key=lambda x : x[-1]), f_list)
print('sort -', f_list.sort(), f_list(key=lambda x : x[-1], reverse=True), f_list)

# list vs array 적합한 사용법 설명
# 업계에서 어떻게 설명할지 많이찾아본 결과 요약하면 아래와 같다.
# list 기반 : 융통성, 컨테이너 타입으로 다양한 데이터 타입을 담을 수있고 범용적 사용
# 숫자 기반 : 숫자 기반일 때는 array를 쓰는게 좋다. 머신러닝, 딥러닝, 기계학습등에서 정말 많은 데이터를 묶어서 고속의 연산을 쓸때
# -> 다만 array(배열)은 리스트와 거의 호환된다.
# -> 숫자로만 구성되어 있다면 array를 쓰는 것을 권장하고
# -> 문자 등 여러 데이터로 구성되어 있으면 list 쓰는 것을 권장한다.
# Json 같은 경우는 딕셔너리로 받을 수 있겠다.

# sort와 sorted의 차이는 반드시 알아두자.