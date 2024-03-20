# 메소드의 세가지
# class, instance, static 
# 이 메소드를 활용해서 실용적인 예제와 실습을 한다음 마무리를 하겠다.

class Car():
    # 코멘트를 달아주기
    """
    Car class
    Author : Rhie
    Data : 2024.03.14
    Description : Class, Static, Instance Method
    """
    # 국내, 국외에 대한 여러자동차 회사들의 과세 비율이 있다하자.
    # 5천만원에1 을 곱해도 어차피 5천만원이다.
    # 하지만 내년에 1.2 상승이 되면 가격 상승이 될 것이다.
    # 아래 price_per_raise 값을 바꾸면서 전체 instance가 영향을 받고
    # 또 계산된 값을 반환하는지, 또 static 메서드를 이용해서 진행할 예정이다.
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
    

    def __str__(self): 
        return 'str {} - {}'.format(self._company, self._details)

    def __repr__(self): 
        return 'repr {} - {}'.format(self._company, self._details)

    # Instance method를 지금까지 self를 통해 활용했었다.
    # self : 객체의 고유한 속성 값을사용했었다.
    def detail_info(self) :
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance method
    # 어떤 차의 가격을 반환해야하는지 알고 있어야 하기 때문에
    # Instance 메서드인 self를 쓰는게 좋다.
    def get_price(self) :
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # 가격이 상승한 다음에 출력되는 메서드
    def get_price_culc(self) :
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')* Car.price_per_raise)

    # 클래스 메소드를 통해서 비율(price_per_raise) 변경해보기
    # 데코레이터를 붙여서 작성해주는데, 처음인자는 cls로 약속되어있다.
    # 아무런 데코레이터가 안붙어있다면 instance 메소드로 자동 인식된다.
    # 여기서 말하는 cls는 앞에서작성한 Car 클래스이다.
    # 우리는 price_per_raise를 인수로 받을 것이므로 per라고 뺀다.
    # 그래서 공통적인 클래스 변수들을 컨트롤 하거나 값을 수정하거나 읽어오거나 엑세스하거나 
    # 읽거나 쓰거나 할 때는 @classmethod를 쓴다.
    # 따라서 @classmethod가 나오면 클래스 변수를 수정하거나 무언가를하겠다라고 이해함 된다.
    # class 변수는 모두가 참조하여 로직에서 매우 중요하다. 따라서 집중해서볼 수있게 @classmethod라는 데코레이터가 달려있다.
    @classmethod
    def raise_price(cls, per) :
        if per <= 1: # 가격이 내려간다면
            print('Please Enter 1 Or More.')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')
    
    # Static 메소드
    @staticmethod
    def is_bmw(inst) : #inst는 정해진 룰이아님/inst 빼도 됨
        if inst._company == 'Bmw' :
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw.'
    
        
car1 = Car('Ferrari',{'color':'White','horsepower':400,'price' : 8000})
car2 = Car('Bmw',{'color':'Black','horsepower':270,'price' : 5000})


#print(car1.detail_info()) # class 함수안에 print가 있는데 또 print가 있어서 none이 나옴
car1.detail_info()
car2.detail_info()

# 그렇다면 가격정보를 어떻게 접근할까?
# 아래처럼 얻을 수 있으나 좋지 못한 접근 방법임.
# 직접 자기의 인스턴스 변수에 접근하는 것은 좋지 못하다.
# 만약 은행에서 이율이 실수로 변경되버리면 어떤상황이 펼쳐지겠는가?

# 가격정보-인상전(직접접근)
print(car1._details.get('price'))
print(car1._details['price'])
# 따라서 보통은 메소드를 만들어서 필요한 정보를 반환하는 방법을 쓴다.

# 가격정보-인상전
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보-인상후
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상 부분을 클래스 부분을 활용해서 변경해보는 실습을 해보겠다.
# 아까 앞에서 직접접근하는건 좋지 못하다 했다.
# Car.price_per_raise = 1.4 부분도 마찬가지다.

# 이렇게 직접 class 문에 접근안하고 따로 메소드를 만드니 로직도 만들 수 있게 되었다. 
# if문으로 체크해서 네가 원하는 값이 들어오지 않으면 리턴하는 이런부가적인 코드도 작성이 가능하다.
# 이렇게 class 변수를 핸들링할때는 class 메소드를 이용하는걸 권장한다.
# 이게 바로 파이썬스러운 코드 작성법이다.

# 클래스 메소드를 통해서만들자.
# Class 메소드 이므로 바로 접근이가능하다.
Car.raise_price(1.6)

# 가격정보-인상후
print(car1.get_price_culc())
print(car2.get_price_culc())

# 마지막으로 Static 메소드를 볼것인데 애매하다.
# instance 메소드는 self를 인수로, class 메소드는 cls를 인수로 받았다.
# 그러나 Static 메소드를 비여있다. 그래서 좀 더 너가 유연한 메소드로 써!라는 느낌이다.
# python static method vs class method 라고 검색해보면 구글이나 많은 개발자들이 이게 정말 필요하냐 라고 토론을 하고있다.
# class method 는 cls가 넘어왔으나 static은 class의 어떤 인자를 받지 못한다.
# static은 메소드를 정의할 때 class 메소드에도 넣기 좀 그렇고 instance 메소드에도 넣기 그렇고...
# 공통적으로 만드는데 유연한건없나? 라고 할때 쓰는게 좋다.


# 만약 이번 로직에서 여러 차들이 만들어졌는데,
# 이차가 Bmw가 맞아? 라는 로직을 넣는다하자.
# class 메소드에 넣기엔 가격 인상만 관련있고..
# instance 메소드에 넣으면 만들 수 있다. 각각의 개체를 for문을돌면서
# 그거에 대한 comapny name이 Bmw인지를 확인하면 된다.
# 하지만 좀 더 포멀하게 전체적으로 아우를 수 있는 메소드를 만들고 싶다하자.
# 자주 쓰이진 않지만 가끔 사용하는거.. 그럴 때 static 메소드를 사용할 수 있겠다.
# Class처럼 쓰이나 self나 cls가 필요가 없을 때 유연하게 사용된다.

# Static method
# 내 자신인 instance를 넘겨야 inst가 car1._company를 위에서 불러오므로 자기자신을 넣는다.
# 인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 또한 신기한 기능이 있는데, 객체로 호출하지 않고 Class 로도 호출이 가능하다.
# 클래스 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

# 여기까지가 보통 블로그가 설명하는 파이썬 기반의 고급 class 기능들을 나열했다.
# 이거보다 더 깊게 들어갈 수 있으나 이정도만 알아도 깃허브나 오픈소스상에서
# 소스코드의 class가 눈에 들어올 것이다.
# 복습을 해서 Method 3개(Class, Instance, Static), 변수 2개(Class, Instance)
# 를 10분 정도만 복습하자. 