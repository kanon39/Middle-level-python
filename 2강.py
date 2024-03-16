# 자동차 코드를 활용해서 클래스 변수와 인스턴스 변수의 차이점
# 클레스 메소드 실습하고
# 네임스페이스 이해

class Car():
    # 코멘트를 달아주기
    """
    Car class
    Author : Rhie
    Data : 2024.03.14
    """
    
    # class 변수 선언 : 차의 갯수가 몇개인지 찍어보겠다.
    #### 핵심포인트 1 -> 클래스 변수는 모든 인스턴스가 공유한다.
    car_count = 0
    
    
    # 기본적인 init이 있어 실행해도 에러발생 안됨
    def __init__(self, company, details):
        self._company = company
        self._details = details
        # init 메서드가 실행될 때마다 car_count 값이 1씩 증가
        # car1의 객체 생성시 1, car2 객체생성시 2가 된다.
        Car.car_count += 1 
        #self.car_count = 10
    
    # __str__ 통해 원하는 클래스 인스턴스 내부의 속성 정보를
    # 내가 원하는 방식으로 출력이 가능하다.
    def __str__(self): 
        return 'str {} - {}'.format(self._company, self._details)

    #__str__ 는 print를 보는 사용자 입장에서 볼때,
    # __repr__는 개발자관점에서 객체고 이 자료형의 타입에 따른 개체를 그대로 표시해줄 때
    # 만약 둘다 사용했을 때 str이 없다면 repr를 출력한다.
    # 둘다 없을 경우 상위정보인 랩핑된 정보만 나옴
    # 두개 다 선언해놓고 보는것도 좋은 방법이다.
    def __repr__(self): 
        return 'repr {} - {}'.format(self._company, self._details)

    def __del__ (self) :
        print("삭제 호출이 됩니까?")
        Car.car_count -= 1 # car_count에서 1을 빼주겠다.

    def detail_info(self) :
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

car1 = Car('Ferrari',{'color':'White','horsepower':400,'price' : 8000})
car2 = Car('Bmw',{'color':'Black','horsepower':270,'price' : 5000})
car3 = Car('Aodi',{'color':'Silver','horsepower':300,'price' : 6000})


# self는 인스턴스 메소드이다. 항상 첫번째 매개변수가 넘어오게 되어 있다.
# self가 있어야 각기다른 객체 car1-car3별로
# 메모리가 관리되는 것을 볼 수 있다.
# 즉 클래스(틀)은 하나지만 찍어내는 것(객체)은 다르다고 볼 수 있다.
# = 각 객체별로 따로따로 관리가 된다는 것이다.
# 이는 각 저장된 메모리 값을 확인하는 id를 통해 확인이 가능하다.
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # 다르다고 나온다
print(car1 is car2) #메모리 주소가 같는지 물어본다. -> False 가 나온다.

#  네임스페이스 확인가능한 dir와 &  __dict__ 비교
print(dir(car1)) # dir은 활용할 수 있는 메소드를 리스트 형태로 보여준다.
print(dir(car2)) # car1와 car2는 같게 나온다(같은 class이기 때문)
# 두개를 실행하면 활용할 수 있는 메소드에
# init에서설정한 _company와 _details를 찾을 수 있다.

print(car1.__dict__) # 내부 class의 값을 딕셔너리 형태로 보여준다.
print(car2.__dict__)
# 즉 dir은 상위로부터 상속받은 모든 것들을 보여주는 반면 값은 보여주지 않는다.
# __dict__은 키와 값형태로 상세하게 보여주고 있고 car1와 car2는 다르게 나온다.
# 즉 class 안을 까볼까? 할 때 개발중에 많이 쓰이는 명령어이다.


# __doc__ 확인
# 우리가 쓰는 keras, tensorflow 등 이게 뭐지 싶은 것들이 있을 것이다.
# 이게 뭐했던 거지 라고 확인할 때 쓰는 메서드이다.
# class 내부에 큰따옴표 3개로 묶여있는 것의 내용이 나온다.
print(Car.__doc__) 

##############################
# 실행
##############################
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
# 여기서 class의 메모리값은 동일하다. 부모는 모두 같기 때문.
print(id(car1.__class__), id(car2.__class__))
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__)) # True 나옴

# 에러
# Car.detail_info() 
# 이때 타입에러인  missing 1 required positional argument : 'self'에러 발생
# detail_info 함수를 보면 첫번째 print에 self id값을 출력하고
# 두번째 print에 self의 company와 price를 출력하는데 인자를 넘기지 않았다.()가 비어있음
# 이때 아래와같이 인자를 넣어주면 오류가 안난다.
# 아래 두 줄은 같은 결과를 산출한다.
Car.detail_info(car3)
car3.detail_info()

# class 내부 변수와 인스턴스 변수(ex. __init__ 내부 변수) 비교
# class 내부 변수에만 생성했을 경우
# class 내부 변수는 아래 __dict__에서는 보이지 않는다.
print(dir(car1))
# 그러나 class 변수를 직접 지정하여 print 하면 값이 보인다.
#print(car1.car_count)

# __init__ 메서드 안에 car_count 변수를 생성했을 경우
# 전체 메소드안에서도 확인이 가능하다.
print(dir(car1))

# 즉, class 변수는 모든 인스턴스가 공유한다. 그러기에 각 개체가 소유하지 못해서 네임스페이스에 안나온다.
# 인스턴스 속성자체가 모두와 공유하기보다는 "내꺼"이므로 car_count를 인스턴스 변수로
# __init__을 통해 추가하게 되면 dir(car1)을 했을 때 car1 객체가 가진 인스턴스 변수 중 하나인
# car_count 변수를 확인할 수 있게된다.
# dir(car1) 해서 네임스페이스를 볼때 class 변수인지, 인스턴스 변수인지 구분하기 위해
# 인스턴스 이름앞에 _를 붙인다. (일종의 약속)

# del 메소드 새로 추가해보기

print(car1.car_count)
print(Car.car_count)


# 삭제 확인
# del 메소드가 del car2 를 통해 호출이 되면 인스턴스를 메모리에서 지웠기 때문에
# 공유된 이미 앞에서 car_count가 3인 값에서  -1을 빼게 되어 2가 된다.

del car2 

print(car1.car_count)
print(Car.car_count)

# 따라서 각 변수를 각 역할에 맞게 선언하는 것이 중요하다.
#### 핵심포인트 2 : 인스턴스 네임스페이스에서 없으면 상위에서 검색한다.
#### 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스변수))
#### 만약 self에 self.car_count = 10 를 해버리면 class의 car_count를 가져오는게 아니라 이미 내 자신이
#### car_count를 가지고 있으므로 2가 아니라 10을 가져온다.
#### 자기꺼(인스턴스)에도 없어? 그럼 상위(class)에서찾어, 그래도 없어? -> 에러
#### 이를 알면 다른 사람 소스코드 이해하는데도 어려움이 덜할 것이다.


