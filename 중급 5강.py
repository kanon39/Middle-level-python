# 이전에 구현한 과일 메소드를 토대로 실무에서 구현할 법한 class를 만들고 실습해보겠다.

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
        

# 클래스  예제2
# 벡터(x,y)이면 x=5, y=2인 크기와 방향을 가진다.
# 파이썬도 수학과 관련된 패키지들이 많다.
# 상황을 가정해보자. 개발을 잘하는 너에게 벡터 계산을 해주는 class를
# 오픈소스로 만들어서 패키지로 배포하는 임무를 맡았다 하자.

# (5,2) + (4,3) = (9,5) 가 된다.
# (10,3) * 5 = (50, 15) 가 된다.
# (5,10) 에서 높은 수를 반환하라 하면 10이 된다.
# Max((5,10)) = 10 
# 쉬워보이지만 지금까지 파이썬 기초, 매직 메서드를 잘 정리하지못하면 
# 구현을 못할 것이다.
# 잘 가져다 쓰는 개발자도 좋은 개발자지만, 개발자를 위한 오픈 소스 개발이
# 더 인정을 받는다.

# 잘따라하면 이시점을 기준으로 실력향상이 많이 될 것이다.

class Vector(object) :
    # 패킹해서 넘어온다고 가정하고 언패킹을 해주겠다.
    def __init__(self, *args) :
        # 아래 주석을 호출하려면 Vector.__init__.__doc__ 이렇게 print 해줘야 된다.
        '''
        Create a vector, example : v = Vector(5, 10)
        ''' 
        # 아무런 값이 들어가지않는다면 예외처리를 따로 해준다
        if len(args) == 0 : 
            self._x, self._y = 0, 0 # 이 또한 언패킹이다 앞에 0 뒤에 0
        else :
            self._x, self._y = args
        
    def __repr__(self) :
        '''
        Return the vector informations.
        '''
        return 'Vector(%r, %r)' % (self._x, self._y) # 앞에 self._x, 뒤에 self._y가 대입됨.
    
    def __add__ (self, other) :
        '''
        Return the vector addtion of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__ (self, number) : # 곱할 값이 y로 들어감 이건 개발자맘
        '''
        '''
        return Vector(self._x *number, self._y * number)
    
    def __bool__(self) :
        # 두 값이 0,0인지 확인하는 메소드
        # 만약 5,3이면 5가 반환되고 boolen 이므로 True가 나옴.
        # 0이면 False 나옴
        if not bool(max(self._x, self._y)) :
            return True
        else :
            return False
    
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직 메서드 출력
# 만약 너의 패키지를 어떤 사람이 처음 다운로드 받는다하자.
# 이때 매직 메서드를 통해 구조를 먼저파악한다.
# doc를 통해 아 이렇게 쓰는거구나를 파악할수 있다.
# v3가 0일 경우 0으로 초기화되도록 확인도 했다.
print(Vector.__init__.__doc__) 
print(Vector.__repr__.__doc__) 
print(Vector.__add__.__doc__) 


print(v1,v2,v3)


print(v1+v2)
print(v1*3)
print(v2*10)
print(bool(v1),bool(v2))
print(bool(v3), bool(v2))
print(bool(v3))

## 있으면 좋겠는데 라는걸 개발하면 10배는 능력이 향상됨.

