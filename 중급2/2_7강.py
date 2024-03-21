# Getter, Setter

"""
Chapter 2
Python Advanced(2) - Property(2) - Getter, Setter
Keyword - @Property

"""

# 그냥 @Property를 검색하면 모른다. 수학처럼 앞을 알아야 뒤를알아야
# 이해되는 학습패턴도 프로그래밍에서도 적용된다.

"""
프로퍼터(Property) 사용 장점

1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter 효과 동등(코드 일관성이 있음)
 - 캡슐화-유효성 검사 기능 추가 용이
 - 대체 표현(속성 노출, 내부의 표현 숨기기 가능)
 - 속성의 수명 및 메모리 관리 용이(제일 중요)
 - 디버깅 용이
 - Getter, Setter 작동에 대해 설계된 여러 라이브러리(오픈소스) 상호 운용성증가
  (예 : Django getter, setter 원리가 잘들어감)
"""

#Ex1 
# Property 활용 Getter, Setter 작성

class SampleA :
    def __init__ (self) :
        self.x = 0
        self.__y = 0 # private
    # 여기서는 프라이빗 변수가 하나라서 다행이지만
    # 아래 처럼 여러 함수들이 존재하게 된다면
    # def get_y(self) :
    #     return self.__y
    
    # def set_y(self, value) :
    #     self.__y = value
    # # 엄청 복잡해질 것이다.
    # 실제 위 코드는 과거의 파이썬 버전은 이렇게 활용되었었다.
    
    # 이 아래가 현재 파이썬의 표준이다.

    # property가 선별하는 프라이빗 변수의 함수명은 모두 변수명과 동일 
    # y 변수의 getter
    @property ## getter
    def y (self) :
        print("Called get method.")
        return self.__y
    
    # y 변수의 setter
    @y.setter ## setter
    def y(self, value) :
        print("Called set method.")
        self.__y = value
        
    @y.deleter  # 이 객체가 메모리를 많이차지하는 데이터일 경우삭제할때 사용
    def y(self) :
        print("Called delete method.")
        del self.__y
        
a = SampleA()

a.x = 1
a.y = 2  # y를 수정하라는거네? -> @y.setter 로 가져옴
a.y  # y를 가져오라는거네? -@property 로 가져옴

print('Ex 1 > x : {}'.format(a.x))
print('Ex 1 > x : {}'.format(a.y))

# deleter
del a.y
print('Ex1 > ', dir(a)) #_SampleA__y 가 사라짐.


# Ex2
class SampleB :
    def __init__ (self) :
        self.x = 0
        
        # private
        self.__y = 0 

    @property ## getter
    def y (self) :
        print("Called get method.")
        return self.__y

    # 만약 아래 __y가 0보다 커야되라고 제약조건을 걸면
    # y.setter 부분을 수정해주면된다. (수정을 받는 부분이므로)
    @y.setter ## setter
    def y(self, value) :
        if value < 0 :
            raise ValueError('0보다 큰 값을 입력하세요.')
        self.__y = value
        
    @y.deleter
    def y(self) :
        print("Called delete method.")
        del self.__y
        
b = SampleB()

b.x = 1
b.y = 10

#b.y = -5 # 예외발생. 

# 있는 것을 개선시키려는 생각이 좋은 개발을 하려는 사람이 많음.
print('Ex 1 > x : {}'.format(b.x))
print('Ex 1 > x : {}'.format(b.y))