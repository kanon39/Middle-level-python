# Shallow & Deep copy

# 가변형, 불변형 shallow, deep copy가 뭔지 실수할 법한 것들을 가지고
# 코딩을 해보겠다.

# 반드시 확실하게 알고 넘어가야 된다.

"""
Chapter 1
Python Advanced(1) - Shallow Copy & Deep Copy
Keyword - shallow & Deep copy

"""
"""
객체의 복사 종류 : copy, shallow Copy, Deep copy
정확한 이해 후 사용 -> 프로그래밍 개발 중요(문제 발생 요소)

가변형과 불변형 : 같은 메모리 주소에 변경된 값이 저장되면 가변형,
안되면 불변형이다.
불변형일 경우, 변수에 하나의 값이 대입되었다가 다른값이 동일한 이름의 변수로 대입되면 메모리주소가 달라짐.
또 같은 변수에 이전과 같은 값을 다시 대입하면 이전과 동일한 메모리 주소가 나옴
가변 : list, set, dict 외 나머지는 불변형

"""

# Ex1 - Copy
# Call by value(값을 바라본다던지),
# Call by Reference(참조값을 바라본다던지),
# Call by Share(share 값을 바라본다던지)
def generate_list(x) :
    return [x for x in range(x,x+3)]

#a_list = generate_list(1)+[generate_list(4), generate_list(7)]
a_list = [1,2,3, [4,5,6], [7,8,9]]
b_list = a_list

# b_list가 a_list와 같은 값을바라볼까?
print('Ex1 > ', id(a_list))
print('Ex1 > ', id(b_list))

b_list[2] = 100
# 나는 복사해서 다른 값을 대입했는데, 같은 아이디값을 바라봄으로써
# 복사된 시퀀스와 원본 시퀀스 모두 영향을 받는 사이드 이펙트가 발생할 수 있다.
# 중첩 리스트도 마찬가지로 사본의 값을 변경하면 원본도 같이 변하게됨.
# -> call by reference
b_list[3][2] = 500

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)

# immutable(불변형) : int, str, float, bool, unicode ...

# Ex2 - Shallow copy(얕은 복사)
import copy

c_list =  [1,2,3, [4,5,6], [7,8,9]]
d_list = copy.copy(c_list)
# 데이터 값이다름. 사본을 만들어서 추가를 할때 경우에 맞게 사용해야 됨.
# -> Call by value
print('Ex2 > ', id(c_list))
print('Ex2 > ', id(d_list)) 
d_list[1] = 100

print('Ex2 > ', c_list)
print('Ex2 > ', d_list) # d_list만 변경되고 c_list는 변경되지 않음을 알 수 있음.

# 하지만!! 중첩 리스트에서는 원본과 사본 모두 값이 바뀜.
# 이는 안의 중첩된 리스트는 같은 아이디값을 바라보고 있기 때문
# -> call by reference
d_list[3].append(1000)
d_list[4][1] = 10000

print('Ex2 > ', c_list)
print('Ex2 > ', d_list) # d_list만 변경되고 c_list는 변경되지 않음을 알 수 있음.

# Ex3 - Deep copy (깊은 복사)
# 정확히 복사이기때문에 느리고 그만큼 또 메모리를 잡아먹는다.

e_list =  [1,2,3, [4,5,6], [7,8,9]]
f_list = copy.deepcopy(e_list)

print('Ex3 > ', id(e_list))
print('Ex3 > ', id(f_list)) # d_list만 변경되고 c_list는 변경되지 않음을 알 수 있음.

f_list[3].append(1000)
f_list[4][1] = 10000

# 정확히 중첩된 리스트도, 밖의 리스트도 깊은복사가 이루어져서
# 복사된 객체 내부 시퀀스 값을 변경하더라도 원본이 변경되지 않게됨.
print('Ex3 > ', e_list)
print('Ex3 > ', f_list)

# 파이썬 하나만 잘해도 다른 언어에 적용하기 쉽다.