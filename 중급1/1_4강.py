# 파이썬 공식 단어로는 스페셜 메소드=매직메소드라고 하는 것을 배울 것이다.
# 빌트-인(built-in)이라고 해서 파이썬 내부에서 처리하는 것들을 
# 직접구현하게 되면 좀 더 low level에서 효율적인 코드를 작성할 수 있게 된다.

# 중급이상 교재에서 설명하는 파이썬 핵심 구조를 설명하겠다.
# Specail method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 이를 알면 파이썬을 알 수 있는 지평이 무궁무진하게 넓어진다.

# 매직 메서드란 클래스 안에 정의할 수 있는 특별한(Built in) 메소드
# 이미 만들어진 것을 사용하는데 좀 더 low level에 해당되는걸 가져와서 활용한다.
# 예로 __init__, __repr__ 등이 있다.
# what is python spceil method 로 구글 검색했을 때 나오는 아래링크의
# https://docs.python.org/3/reference/datamodel.html 
# 레퍼런스 내 데이터모델은 진짜 진짜 중요한 것이다.
# Cpython에서도 개발이 가능하다면 몸값도 올라가고
# 일반적으로 하는 취미, 대학교 수준의 다른차원의 개발자, 엔지니어가 되는 것이다.

# 클래스의 연장 수업이며 파이썬의 핵심을 학습 순서로 다시 나열하면
# 지금까지 하면 class가 마무리가 되는 것이고
# 다음 챕터해서 시퀀스를 할것이고
# 시퀀스를 알아야 반복을 할 수 있다.
# 그 다음 1급 함수의 개념을 알아야 
# 반복과 같이 클로져나 코루틴을 할 수있다.
# 유기적으로 연관되어 있다. 

# 기본형
# 지금까지 생각하지 않고 사용했던 모든 데이터 타입이 class이다.
print(int) 
print(float)

# 모든 속성 및 메소드 출력
# 이 dir을 했을 때 나오는 이미 만들어져있는 메소드들을 구현만 해주어도
# 좀더 low-level에서 개발이 가능하다는 것이다.
print(dir(int))
print(dir(float))

n = 10
# n에다가 10을 넣은 n도 class이다.
print(type(n))

# n에다 100을 더해보자.
# 이렇게 100이 더해졌다는 것은 class int안의 __add__가 호출되었다는 것이다.
print(n+100)
# 즉 메소드이므로 아래처럼 해도 위와 같은 결과가 나온다.
print(n.__add__(100))
# 이제이 int class에 대한 문서 내용을 확인해 보겠다.
#print(n.__doc__)
# 0이면 False, 0이 아니면 True를 호출하는 함수도 아래와같다.
print(bool(n), n.__bool__())
# n에 100을 곱한다하면
print(n*100, n.__mul__(100))

# 파이썬이 사람들이 쓰기 쉽게 랩핑해서 쓴다는 것을 알 수 있고
# 나는 곱하기를 했는데 더해지는 이런 나만의 클래스를 만들 수도 있다.

print()
print()

# 클래스 예제1
# 과일이 여러개가 있는데, 학생+학생하면 우리가 정의하기로,
# 두 학생을 더하면 키를 더한다거나 할 수도 있고
# 구현하고자 하는 로직을 넣을 수 있게 된다.

# 클래스 예제1
class Fruit :
    # init 메서드는 생성메서드니까 초기화를 해주자
    # 과일의 이름과 가격을 받겠다.
    def __init__ (self, name, price):
        self._name = name
        self._price = price
        
    def __str__ (self) :
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)
    # 스페셜 메소드를 활용한 더하기 메소드 구현
    # 더해준다는건 어떤게 들어와서 더해진다는 의미이므로
    def __add__(self, x) :
        print('called >> __add__')
        return self._price + x._price
    
    # 스페셜 메소드를 활용한 빼기 메소드 구현
    def __sub__(self, x) :
        print('called >> __sub__')
        return self._price - x._price
    
     # 스페셜 메소드를 활용한 앞기준 작거나 같은지 메소드 구현
    def __le__(self, x) :
        print('called >> __le__')
        if self._price <= x._price :
            return True
        else :
            return False
        
      # 스페셜 메소드를 활용한 앞기준 크거나 같은지 메소드 구현
    def __ge__(self, x) :
        print('called >> __ge__')
        if self._price >= x._price :
            return True
        else :
            return False          
    
# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)
s3 = Fruit('Mango', 2000)
# 만약 매직메서드 __add__ 를모른다면 아래와 같아질 것이다.
# 그러나 아래처럼 접근하는 것은 좋지 못하다고 했다.
#print(s1._price + s2._price)

# 우리는 add 메소드를 구현을 했기 때문에 두 변수 사이에 +가 들어가면
# 자동으로 __add__ 메소드를 호출하게 된다.
# 만약 여기에 80% 할인 세일된다하면 아래값을 수정만하면된다.
print(s1+s2)

# 앞서 구현한 빼기, 작거나같다, 크거나 같다 구현해보기
print (s1 >= s2)
print (s1 <= s2)
print (s1 - s2)
print (s2 - s1)

# 우리가 지정한 str 메서드가출력됨.
print(s1)
print(s2)

# 매직 메서드를 활용하면 더하기 빼기 등 다 구현이 되어있다.
# class 내부에 원래 더하기의 본연의 기능에 우리가 추가로 기능을 구현할 수 있다.
# class로 구현되어 있어서 유지보수도 쉽다.

# 이 모든 것, 파이썬 핵심구조, 매직 메소드 ,클래스 매직 메소드 실습
# 이 과정을 파이썬 데이터 모델이라고 부른다.