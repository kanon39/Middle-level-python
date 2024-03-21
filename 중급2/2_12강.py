"""
Type inheritance
Custom Meta Class
메타 클래스 상속 실습
"""

"""
Chapter 3
Python Advanced(3) - Metaclass(3)
keyword - Type inheritance, Custom metaclass

"""

"""
메타클래스 상속
1. type 클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
  - 클래스 생성 가로채기(intercept)
  - 클래스 수정하기(modify)
  - 클래스 개선(기능추가)
  - 수정된 클래스 반환
"""

# Ex1
# 커스텀 메타클래스 생성 예제(Type 상속 없이)
# class가 아님에도 def 첫번째 인자에 self로 만들어보자.
# 이렇게 메타 클래스에서 활용되는 함수들을 class 내부가아니라
# 밖에 이렇게 쫙 빼놓고 뷔페에서 빼먹듯 메타클래스 사용시마다 꺼내 쓸 수도 있다.
def cus_mul(self, d) :
    for i in range(len(self)) :
        self[i] = self[i] * d # 기존 변수에 곱한값 업데이트

def cus_replace(self, old, new) :
    while old in self :
        self[self.index(old)] = new

# list를 상속받음, 메소드 2개 추가한 메타클래스를 만들어 보겠다.
# 메타클러스는 흑마법ㅋㅋ

CustomList1 = type('CustomList1',
                   (list,), # 기본 자료형 list 타입을 받았기에 list 타입 대입이 가능해지며,
                            # 이로써 리스트와 관련된 모든 함수를 쓸 수 있게된다.
                   {
                       'desc':'커스텀 리스트1',
                       'cus_mul':cus_mul,
                       'cus_replace':cus_replace
                    }
                   )

# CustomList1 가 어떠한 기능을 하는가?
# self라는 값은 항상 매개변수 첫번째를 받는다.
# 따라서 클래스에서 self 로 리스트를 받으려면 첫번쨰에 리스트가 들어가야 된다.

c1 = CustomList1([1,2,3,4,5,6,7,8,9]) # 이 리스트가 self
c1.cus_mul(1000) # 이게 old
c1.cus_replace(1000, 'haha') # 이게 new
print('Ex1 > ', c1)

print('Ex1 > ', c1.desc)
print('Ex1 > ', dir(c1))


# Ex2
# 커스텀 메타클래스 생성 예제(Type 상속 받아보자.)

# class MetaClassName(type) :
#     def __new__(metacls,name,bases,namespace) :
#         코드

# 아래처럼되어 있을 때 실행순서는
# type을 상속받는 순산부터 new > init > call 순서로 커스텀 가능
# 여기까지 안해도됨. 저 위까지 ex1까지만 해도 차고넘침.
def cus_mul(self, d) :
    for i in range(len(self)) :
        self[i] = self[i] * d # 기존 변수에 곱한값 업데이트

def cus_replace(self, old, new) :
    while old in self :
        self[self.index(old)] = new
        

class CustumListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__ (self, object_or_name, bases, dict) :
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict) # type에게 이 3개를 넘겨줌
        # print를 이와같이 찍어보면 __new__의 딕셔너리가 __init__으로 넘어옴을 알 수있다.
        # 이때 이 딕셔너리를 수정하는 것을, 잡아채서 수정한다하여 '후킹'이라고 부른다.
    # 인스턴스 실행    
    def __call__ (self, *args, **kwargs) : # 파라미터가 넘어옴
        print('__call__ -> ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs) # type에게 이 3개를 넘겨줌

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__ (metacls, name, bases, namespace) :
        print('__new__ -> ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀리스트2' # namespace안에 우리가 위에서 했던 함수들을 재사용함
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        
        return type.__new__(metacls, name, bases, namespace) # new는 이렇게 만들어졌으니까 리턴을 해줘야 된다.
    
# 결과는 Ex1와 Ex2와 동일하게나옴. Ex1의 원리가 Ex2임. 동일한 원리임.
    
CustomList2 = CustumListMeta('CustomList2',(list,),{}) # 이미 {}에 __new__의 namespace에서 함수들은 다 넣어둠

c2 = CustomList2([1,2,3,4,5,6,7,8,9])
c2.cus_mul(1000)
c2.cus_replace(1000,7777)

print('Ex2 > ', c2)
print('Ex2 > ', c2.desc)

# 상속 확인
print(CustomList2.__mro__) # 오른쪽에서 왼쪽 순