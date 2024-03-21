# django같은 것도 meta class를 가지고 개발이 되었다.
"""
1. Type(name, base, dct)
2. Dynamic Metaclass
3. 메타클래스 코딩 이점
"""

"""
Chapter 3
Python Advanced(3) - Metaclass(2)
keyword - Type(name, base, dct) # 매개변수 3개넘겨서 클래스 생성가능

"""

"""

메타클래스
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점

"""

# Ex1
# type 동적 클래스 생성 예제
# 메타 클래스는 인자 3개를 받는데, 이름(Name), Bases(상속)-튜플, Dct(속성, 메소드)

# class를 정적으로 만듦
class Sample1() :
    pass

# class를 동적으로 만듦 위의 클래스와 같음.
s1 = type('Sample1', (), {})

print('Ex1 > ', s1) # s1 자체가 sample1 의 class고
print('Ex1 > ', type(s1)) # sample1의 타입은 type class이다.
print('Ex1 > ', s1.__base__) # 모든 클래스는 오브젝트를 상속 받는다.
print('Ex1 > ', s1.__dict__) 

# 동적 생성 + 상속
# class Sample2(Parent1) :
#     attr1 = 100
#     attr2 = 'hi'
# 위와 같은 클래스를 s2로 구현해보겠다.

class Parent1 :
    pass

s2 = type('Sample2', # class 명
          (Parent1,),  # class 부모명 , 꼭 추가 주의
          {'attr1':100, 'attr2':'hi'} # 속성, 메소드
          )


print('Ex2 > ', s2)
print('Ex2 > ', type(s2))
print('Ex2 > ', s2.__base__)
print('Ex2 > ', s2.__dict__)
print('Ex2 > ', s2.attr1, s2.attr2)

# 이렇게 class를 동적으로 만들어 낼수 있게 된다.
# 만약 class하나하나가 DB와 맵핑이 되어 있다면 동적으로 데이터를 생성해내므로
# 프레임워크를 만들때 사용할 수 있는 문법이 된다.

print()
print()

# Ex2
# type 동적 클래스 생성 + 메소드

class SampleEx :
    attr1 = 30
    attr2 = 100
    
    def add(self, m, n) :
        return m + n
    
    def mul(self, m, n) :
        return m * n
    
ex = SampleEx()

print('Ex2 > ', ex.attr1)
print('Ex2 > ', ex.attr2)
print('Ex2 > ', ex.add(100,200))
print('Ex2 > ', ex.mul(100,20))

# 위를 동적으로 만들어 보겠다.
print()
print()

s3 = type('Sample3',
          (),
          dict(attr1 = 30, attr2 = 100, # 다른 형태의 dict
               add = lambda x, y : x + y, # 잠시 쓸 함수이므로 lambda 활용
               mul = lambda x, y : x * y)
          )
print('Ex2 > ', s3.attr1)
print('Ex2 > ', s3.attr2)
print('Ex2 > ', s3.add(100,200))
print('Ex2 > ', s3.mul(100,20))