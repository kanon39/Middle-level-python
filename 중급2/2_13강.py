#  Descriptor 는 getter, setter 의 로우레벨에서 작동되는 것.

"""
chapter 3
pyton Advanced(3) - Descripter(1)
Keyword - descriptor, set, get, del, property

"""

"""
디스크립터
1. 객체에서 서로다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리정의 가능
3. data descriptor(set, del)->변경, non-data descriptor(get)->읽기만함
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""

# Ex1
# 기본적인 Descripor 예제
# __init__, __get__, __set__, __Delete__ 는 정해진 예약어다.
class DescriptorEx1() :
    def __init__ (self, name='Default') : # name에 아무것도 안들어오면 ;Default가 들어옴
        self.name = name

    def __get__ (self, obj, objtype) :
        # Django를 쓸 때 DB와 1:1매핑할때 이런 기능을 사용하면 
        # 나중에 이를 추후 활용할 때 따로 커넥션 신경 또 안써도됨
        return 'Get method called. -> self : {}, obj : {}, objtype : {}. name : {}'.format(self, obj, objtype, self.name)
    
    def __set__ (self, obj, name) :
        print('Set method Called.')
        if isinstance(name, str) : # 만약 이름이 문자인지 확인
            self.name = name
        else :
            raise TypeError('Name should be string')
        
    def __delete__(self, obj) :
        print('Delete method called')
        self.name = None
# https://realpython.com/python-descriptors/ 이 사이트의 D.R.Y code 부분
# 예전에 getter, setter를 할때  @property를 하더라도 변수갯수만큼 함수가 많아진다.
# 이제는 위처럼 DescriptorEx1만 할당하면 되니까 코드도 간결해지고 재사용성이 좋아짐.
# 그리고 0이상만 넣는다던지 비즈니스 로직도 삽입이 가능해졌다.
# 이제 아래 Sample1 class의 name을 핸들링할 때는 위의 DescriptorEx1이 알아서 호출된다.
# 즉 이 name을 수정할 때는 set이 호출되고 지울떄는 delete가 호출된다.

class Sample1() :
    name = DescriptorEx1() # 선언안했으므로 name은 default가 있음.

s1 = Sample1()
s1.name = 'Descriptor Test1' # set mothod가 실행됨.
# s1.name = 10 # 우리가 만든 문자만들어가야되는 예외발생
# 즉 객체생성 컴퓨터에 사용자가 요청 ----> 객체 생성 이 사이의 과정을 descriptor가 통제하게된다.
print('Ex1 >' , s1.name)

print()
print()
# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print('Ex > ', s1.name)
print()
print()

# 위에서는 아래처럼 다른 클래스에서 선언을 해서 사용했었다.
# class Sample1() :
#     name = DescriptorEx1()
# 하나의 클래스에서 사용하는 방법도 있음.

# Ex2 
# Property 클래스 사용 Descriptor 직접 하나의 클래스에서 구현
# 파이썬 공식문서에 아래처럼 되있다.
# class property(fget=None, fset=None, fdel=None, doc) # None 은 기본값

class DescriptorEx2 (object) :
    def __init__(self, value) :
        self._name = value
    
    def getVal(self) :
        return 'Get method called. -> self : {}, name : {}'.format(self, self._name)
    
    def setVal(self, value) :
        print('Set method called.')
        if isinstance(value, str) :
            self._name = value
        else :
            raise TypeError ('Name should be string ^^')
    
    def delVal(self) :
        print('Delete method called.')
        self._name = None
    # ex1에서는 사용 클래스 별도로 했으나
    # property 클래스와 사용 클래스를 하나로 함.
    name = property(getVal, setVal, delVal, 'Property Method Example^^')
    
# 최초 값 확인
s2 = DescriptorEx2('Descriptor Test2')

print('Ex2 > ', s2.name)

# setval 호출
s2.name = 'Descript Test2 ^^'

# 예외 발생
#s2.name =10

# getval 호출
print('Ex2 >', s2.name)

#delVal 호출
del s2.name

# 재확인
# getVal 호출
print('Ex2 >', s2.name)

# Doc 확인
print('Ex2 > ', DescriptorEx2.name.__doc__)