# Descriptor 예제 심화
"""
chapter 3
pyton Advanced(3) - Descripter(1)
Keyword - high level property(get, set) vs low level descriptor(get, set 생성시점)

"""

"""
디스크립터
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
(파이썬에서는 class = 객체, 모든 정수하나 선언도 class임)
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용
"""

# Ex1
# Descript 예제(1)

# 현재 이 파이썬 파일이 저장된 폴더 내 파일 갯수를 가져오는 기능을 써보겠다.

import os
# [개발 1단계] : Directorypath에서 경로를 받아서
# DirectoryFileCount가 descripter처럼 활동해서 파일의 갯수 리턴
class DirectoryFileCount :
    pass

class DirectoryPath :
    pass

# [개발 2단계] : 
class DirectoryFileCount :
    # 우리는 파일을 수정하진 않으므로 __get__ 메서드만 가져올것이다.
    def __get__(self, obj, objtype=None) : # print할시 나옴
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname)) # os 경로내 리스트 원소수를 리턴함.
        # 여기까지가 descripter 구현이 끝났다.
        # 단 여기서 self는 DirectoryPath의 dirname이 obj로 넘어간것이다.
        # 즉 descripter를 사용하는 객체의 어떤 인스턴스 변수를 접근할 떄는 obj로 넘어간다.
class DirectoryPath :
    # Descripter instance
    size = DirectoryFileCount()
    
    def __init__(self, dirname) :
        self.dirname = dirname
        
# 현재 경로
s = DirectoryPath('./')
# 이전 경로
g = DirectoryPath('../')

g.size

print(s.size)

# 헛갈릴 떄 출력 용도
print('Ex1 > ', dir(DirectoryPath))
# 네임스페이스 출력시 size에 DirectoryFileCount라는 class 주소를 가르키고 있다.
print('Ex1 > ', DirectoryPath.__dict__) 
# 좀더 정확하게 파악하려면 인스턴스의 네임스페이스가아닌 
# 클래스에서 네임스페이스를 보는게 더 정확하다.
# 여기서 size가 어떤 클래스를 가르키고있구나 하고 이 클래스를 막찾을 것이다.
# (지금은 위에다 선언을 해두었지만..)

print('Ex > ', dir(s))
print('Ex > ', s.__dict__)

# Ex2
# Descriptor 예제2
import logging
# logging 클래스를 호출할 때는 탬플릿을 만들어 놓는게 좋다.
logging.basicConfig(
    format='%(asctime)s %(message)s',
    level = logging.INFO, # 로그의 수준이 5단계가 있다 (이후찾기)
    datefmt = '%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess :
    # descriptor 관리하는 것 만들겠다.
    # score와 관련된 정보를 접근하면 공통적으로 로그 출력등이 가능하게 됨
    def __init__ (self, value=50) :
        self.value = value
    
    def __get__(self, obj, objtype=None) :
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value # get은 return 값이 있어야 됨. 꺼내오는 거니까
    
    def __set__(self, obj, value) : 
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value

class Student :

    # 성적은 예민하니 따로 관리하겠다
    # -> 접근 로그를 남기겠다. 
    score = LoggedScoreAccess()
    
    def __init__ (self, name) :
        # Regular instance attribute
        self.name = name

s1 = Student('Kim')
s2 = Student('Lee')

# 점수 확인
print('Ex2 > ', s1.score)

# 누가 고의로 접근하여 점수를 올렸다하면
# s1의 score에 접근했을때 로그발생,
# s1의 score을 업데이트 했을 때 로그발생
# 여기에 DB와 연결하면 자동업데이트가 될 것이다.
s1.score += 20
print()
print()

# vars는 인스턴스 딕셔너리 정보를 알려주는 키워드
# 결과 {'name': 'Kim'}
print('Ex2 > ', vars(s1)) 
print('Ex2 > ', vars(s2))

# 위와 비슷한 기능을 하는 것 출력
print('Ex2 > ', s1.__dict__) 
print('Ex2 > ', s2.__dict__)