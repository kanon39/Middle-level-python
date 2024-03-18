# 일급함수 - 클로저
# 파이썬의 변수 범위(Scope)
# Global 선언
# 클로저 사용 이유
# Class -> Closure 구현
# 클로저를 잘해놔야 뒤의 병행성, 동시성을 배울 수 있다.

# 클로저 기초

# 1. 파이썬 변수 범위(scope)

# 예제1
def func_v1(a):
    print(a)
    print(b)
    
#func_v1(10) # b를 못찾았다고 에러가 날 것이다.

# 예제2
b=20 #global
def func_v2(a):
    print(a) #local
    print(b)

func_v2(10) # 이경우 10과 20이 출력됨.


# 예제3
c = 30
def func_v3(a):
    c = 40 # 하지만 c=40 이 위에있으면 실행 가능하다.
    print(a) #local
    print(b)
    #print(c) # 위에 글로벌로 지정이 되어 있어도 안에 같은 이름의 변수가 있다면 로컬변수로 인지를 한다.
    # 만약 c= 40이 아래에있다면 print(c)는 실행이 안된다.
    #c = 40
print(c)
func_v3(10)

# 이때 함수안에 global c를 지정해주면 print 아래에 로컬 c가 있으므로 
# 로컬 c가아닌 글로벌 c가 프린트 된다.

c = 30
def func_v3(a):
    global c
    print(a) #local
    print(c) # 이떄는 print(c)가 실행이된다.
    c = 40
print('>>',c) # 여기서 c는 글로벌 c로 출력된다.
func_v3(10)
# 단, 이렇게 함수안에 global을 넣어서 짠 코드는 좋은 코드가아니다.
# 실수의 가능성이 올라감. 함수의 본연의 기능이 끝나면 보통 다 사라져야되는데, 
# 함수가 전역변수와 계속 연관이있다면 디버깅할 때 쉽지 않아진다.



# 이런 변수의 scope에서 클로저의 개념이 시작된다.

# 2. Closure(클로저) 사용이유
# 클로저는 scope가 닫혀도 값을 기억한다는게 포인트이다.
# 이 함수가 실행이 끝나면 선언된 로컬 변수들은 함수가 실행완료되면 소멸이되나 
# 클로저는 기억하게 된다.

# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 한정된, 같은 메모리 공간에 여러자원이 접근하기 때문
# -> 교착상태(Dead Lock) : 다 일을못해버리는 상태를 처리해줘야되기 때문에 
# 상당히 안정되고 검증된 오픈 소스를 활용한다. (Java는 톰켓, 파이어플라이 등)
# 예를들어 네이버의 경우 지진이 났을 때 동시 접속이 초당 300만이 올 경우
# 여러 예외가아닌 에러가 발생해서 서버가 다운됬었다.
# 스레드를 사용하기 때문에 어렵다.

# 파이썬에서는 이런 데드락을 없애기 위해 메모리를 공유하지 않고 메모리 전달로 처리하기위한
# -> ErLang
# 이때 클로저를 사용하여 이전 일들을 기억하여 처리한다.
# 예로 1번 프로그램이 진행중이다 다 끝나면 2번 프로그램들어와, 2번 50%진행됬어, 3번 프로그램 들어와 이렇게 진행한다.
# 따라서 어디까지 일했는지 기억해야 다음에 동일한 프로그램으로 일을해도 처음부터 다시 시작안해도된다.
# 파이썬에서 클로저는 공유하되 변경되지 않는다.(Immutable 또는 Read only)이다. 변경되지 않게 적극적으로 사용한다.
# -> 이는 함수형 프로그래밍과 연결이 된다.

# 결론 : 여기서 배울 클로저는 불변자료구조 및 atom(일관성), STM 이를 통해서 멀티스레드 프로그래밍에 강점을 제공한다.
# 우린 다음에 멀티스레드를 사용하지 않고 코루틴이라는 것을 이용할 것이다. 
# 단일 스레드 환경에서도 멀티스레드 인것처럼 병행성을 동시에 처리할 수 있는 기반을 마련할 수 있다.
# 클로저를 알아야 데코레이터, 코루틴을 알게된다.

# 따라서 클로저는 불변상태를 기억한다 라는 것을 기억하자.
print()
print()

a = 100
print(a+100)
print(a+1000)

# 만약 위의 값을 누적해서 출력해주고 싶다면 
# 결과누적 함수를 이용하면된다.
print(sum(range(1,51)))
print(sum(range(51,101)))

# 그러면 우리가 print문을 계속실행할때마다 계속해서 누적되서 평균을 내주는 로직을 짜보자.
# 3. 클로저 클래스 이용

class Averager :
    def __init__ (self) :
        self._series = []
        
    def __call__ (self, v) : #클래스를 함수처럼 쓸 수 있는 메서드 call
        self._series.append(v)
        print('inner >> {} / {} '.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
 
# 인스턴스 생성
average_cls = Averager()
print(dir(average_cls)) # call 이있으므로 함수처럼 호출 가능

# 누적
print(average_cls(10))
print(average_cls(30))
print(average_cls(50))
print(average_cls(193)) # 값의 상태를 _series라는 변수가 계속해서 기억하고 있다.

# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사후 저장 후에 접근(엑세스 가능)=> 클로저 
# 클로저 함수 조건
# 1) 어떤 함수의 내부 함수일것
# 2) 그 내부 함수가 외부 함수의 변수를 참조할 것
# 3) 외부 함수가 내부 함수를 리턴할것.


# 5. 클로저 심화(Closure) -  Closure 사용방법
# 위에서는 class로 클로저를 구현했으므로 이제는 함수로 클로저를 구현해 보겠다.
# 패턴으로 외워보자.
def closure_ex1() :
    # Free valiable  자유 변수 : 내가 사용하려는 함수(averager) 바깥에서 사용한 변수를 자유변수라함
    # 클로저영역
    series = []
    def averager(v) :
        series.append(v)
        print('inner >>> {}/{}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager  # 함수 자체를 호출

avg_closure1 = closure_ex1()
print(avg_closure1) # 함수로 호출됨을 확인할 수 있다.

print(avg_closure1(30))
print(avg_closure1(40))
print(avg_closure1(50)) # 누적된 값을 계속 추가해서 리턴하게됨.

print()
print()

# 파이썬에서 클로저를 어떻게 취급하는지 Namespace, dir 명령어로 확인해보자.
# function inspection 함수 조사 순서
# 1)여러 매직함수들이있음을 확인
print(dir(avg_closure1))
print()
# 2) code 보니 디테일한 구현가능한 함수가 보이나 co가 붙은 것들이 보인다. co_freevars도 자유변수도 보인다.
print(dir(avg_closure1.__code__))
# 3) 자유변수를 출력해본다. 위에서는 자유변수인 series를 co_freevars에서 파이썬을 가지고 있다.
print()
print(avg_closure1.__code__.co_freevars) 
# 4) 그렇다면 closure에 무엇이 있나 출력해보기
print(avg_closure1.__closure__)
# 5) closure안에 cell_contents를 보면 안에 어떤 값들이 있는지 볼 수 있다.
print(dir(avg_closure1.__closure__[0]).cell_contents)

# 잘못된 클로저 사용

def closure_ex2() :
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1 # 요부분이 len(series) 
        total += v # 요 부분이 위에서의 sum(series) 가 된다.
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# 아래 경우 cnt+=1에서 cnt는 averager 영역이기 때문에 위의 cnt를 참조하지 못해 예외가발생한다.
# print(avg_closure2(10)) 

# 올바른 클로저 사용
def closure_ex3() :
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        # 아래처럼 nonlocal 예약어를 선언해주면 된다. 그럴경우 cnt와 total은 free 변수가 된다.
        nonlocal cnt, total
        cnt += 1 # 요부분이 len(series) 
        total += v # 요 부분이 위에서의 sum(series) 가 된다.
        return total / cnt
    return averager

avg_closure3 = closure_ex2()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))
