# 읽기 전용 딕셔너리에 대해서알아보도록 하겠다.
# 해시 테이블(Hashtable)
# Immutable Dict 생성
# 지능형 Set
# Set 선언최적화

# 해시 테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 안함, 
# set-> 값 중복 허용 안함.

# Dict 및 Set 심화

# immutable Dict

from types import MappingProxyType 
# 이를 활용하면 읽기 전용(추가 수정 불가)을 만들 수 있다.
# d 안의 값을 변경하게되면 안되는 상황이라면
# 이를 아예막아버리는 방법도 있을 것이다.

d = {'key1':'value1'}

# Read only
# 외국에서는 frozen이라고 얼려둔다고 표현하더라.
d_frozen = MappingProxyType(d)

print(d, id(d)) # 딕셔너리는 수정가능하므로 hash가 불가능하다.
print(d_frozen, id(d_frozen)) # d_frozen 또한 hash 불가능하다.

# 수정불가
#d_frozen['key2'] = 'value2' 

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

# 집합 자료형 
s1 = {'Apple','Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple','Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3} # 하나의원소일때 이렇게해도 set으로 선언됨.
s4 = {} # 원소가 하나도 없을 경우 딕셔너리로 선언되버림
s4 = set() #이렇게 해야 집합으로 선언됨
s5 = frozenset({'Apple','Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon') # 멜론추가됨

# 추가 불가
# s5.add('Melon')

# 따라서 딕셔너리에도있고 집합에도 읽기전용 타입이 존재함.

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 자바가 컴파일해서 컴파일된 파일을 놓고 컴파일된 파일을 실행하는것 처럼
# 파이썬에서도 바이트 코드 -> 파이썬 인터프리터 실행
# dis 모듈을 보면 바이트 코드가 어떻게 생성되는지 순서를 볼 수 있다.
from dis import dis

# 위에서 만든것처럼 s1이 빠를까 s2가 빠를까?

print('----------')
print(dis('{10}')) # 이경우 LOAD->BUILD->RETURN 3가지 과정을 거친다.
print('----------')
print(dis('set([10])')) # 이경우 LOAD NAME -> LOAD_CONST->BUILD->CALL->RETURN 6개 과정을 거친다.

# 따라서 s2보다 s1이 더 빠르다.

# 지능형 집합(Comprehending Set)
# -> 집합안에 for문 넣기
print('----------')

from unicodedata import name
# 유니코드의 반환문자값을 보기 위해서 위 패키지 임포트
# name이 값이 있다면 char(i)이고 없다면 공백처리
print({name(chr(i), '') for i in range(0,256)})