# Meta class 이건 왜 쓰는걸까? 하는 이해하는데 기간이 오래걸림.
# 개발을 하는순간 이해가 됬었고
# 이래서 한언어를 깊게 파야되는 구나를 느끼게해줬었던(강사님이)
# 언어에 대한 이해력이 폭넓게 증가했다.
# 언어를 깊게 배운다는게 정말 큰 무기를 가지는 것이다.

# 기술기반의 회사일 경우 이런 것들은 필수다.

"""
Chapter 3
Python Advanced(3) - Metaclass(1)
keyword - Class of class, Type, Meta Class, Custom Meta Class

"""
"""

왜? 메타 클라스를 쓰는가
1. 클래스를 만드는 역할 ->파이썬에서 클라스를 만들어지는 과정에 내가 개입하겠다!
-> 그래서 내가 의도하는 대로 클라스를 커스텀하겠다.
2. 프레임워크 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증 클래스 등을 만들게 해줌.
5. 엄격한 class 사용 요구(프레임 워크 작성하기 때문), 메소드 오버라이드 요구

"""

# Ex1
# type 예제
# 아래 3줄이지만 많은 의미를 가지고 있다.
# 객체지향프로그램에서 오브젝트(개체)란 마우스, 키보드 등 오브젝트다.
# 파이썬에서는 클래스와 객체라는 용어를 같이 사용한다.
# 앞으로는 클래스라고하던 오브젝트라고 하던 같은의미라고
# class == object라고 받아드리면 된다. (공식문서 피셜)
# 파이썬에서 클래스는 클래스 이상의 존재(객체)이다.
# 그래서 이 SampleA라는 클래스를 obj1 변수에 할당하는 순간 모든언어에서 클래스를 인스턴스화 했다라고 부른다.
# 따라서 이 인스턴스화가 되려면 당연히 class문이 메모리에 올라가야된다.
# 그래야 이 class 메모리를 참조해서 인스턴스화를 시킨다.
# 이렇게 인스턴스화가된 객체는 변수의할당, 복사 가능, 새로운속성, 함수의 인자로 넘기기 가능해진다.
class SampleA() :
    pass

obj1 = SampleA() # 변수의할당, 복사 가능, 새로운속성, 함수의 인자로 넘기기 가능

# 클래스가 객체이므로 인스턴스를 붕어빵처럼 찍어낼 수 있다.
# 그렇다면 객체는 어떤 역할을 하는가?
print('Ex1 >', obj1.__class__) # obj1 인스턴스는 sampleA의 class로 만들어짐
print('Ex1 >', type(obj1)) # 타입함수에 obj1의 자료형을 볼때도 SampleA 클래스에요 라고 알 수 있다.

# 그렇다면 이 type에서 확인할 수 있는 class를 만들어내는 class는 뭐냐?
# 어떤원리로 class가 만들어졌는가?
# 이를 볼때 class에 class를 한번 더붙인다
# 바로 class type이 나온다.
print('Ex1 >', obj1.__class__.__class__)

# 즉 모든 class는 파이썬에서 모든 class의 메타, 원형이 되는 것이 type 이다.
# class type이라는 클래스가 모든 class의 meta class이다.
# 이를 이용해서 동적, 정적 클래스를 우리가 만들 수 있을 것이다.
# 동적과 정적의 차이 : 어떤 함수를 만들었을 때 이 함수 실행 중에 함수를 추가할 수 있나? 없다.
# -> 이를 정적이라 한다. 하지만 type class를 이용하면 실행 중에 함수도 추가하고 속성도 추가하고 
# 상속도 추가하고, OMR 프레임 워크 등은 meta class를 사용할 수 밖에 없다.

# 따라서 모든 class의 meta는 type class 이다. 이걸 이해해야 한다.
print(type.__class__) # 핵심

# 위 SampleA를 다시 정리하면 아래와 같다.
# obj1는 SampleA의 인스턴스다.
# SampleA는 type metaclass이다.
# type은 자기 자신이 meta class이다.
# 이 type은 Cpython 레벨에서 구현해둔 것임.

# Ex2
# type meta (Ex1 증명)

# 구현할 때 편하게 사용했던 int, dict

n = 10
d = {'a':10,'b':20}

class SampleB():
    pass

obj2 = SampleB()

for o in (n, d, obj2) :
    print('Ex2 > {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))
    
print()

for t in int, float, list, tuple :
    print('Ex2 >', type(t))
    
print('Ex2 > ', type(type))


    