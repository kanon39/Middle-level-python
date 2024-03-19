# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
# -> 잠깐 공부하다가 멈추고 밥먹고 다시돌아와서 공부하는 것
# -> 내가 어디까지 했는지 알아야 함(클로저)
# -> 단일 프로그램안에서 여러 일을 쉽게 해결할 때 씀
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행
# -> 여러 프로세스나 워커가 동시에 수행
# -> CPU는 하나지만 여러일을 동시에 해내는 코루틴 등이 있다.
# -> 속도


# 1. 병행성 - 코루틴(Coroutine), Yield
# 코루틴 : 단일(싱글) 스레드, 스텍을 기반으로 동작하는 비동기 작업
# -> 단일 스레드 에서도 여러가지 순차적으로 상호작용하면서 블록되지 않고 
# 작업을 수행할 수 있는 것을 뜻하며 파이썬에만 있지않고 다있다.

# *스레드 뜻 : os가 관리하고 동시에 각자맡은작업, 한가지작업을 하는 일할수 있는 리소스가 많은 상태다.
# *스레드 : 싱글쓰레드 -> 멀티스레드 -> 코딩이 복잡 -> 공유되는 자원이 많아져 교착상태가발생 가능성,
# -> 컨텍스트 스위칭 비용이 큼(1번스레드가일하다가 2번 스레드로 제어권을 넘기는 등 스레드끼리 전환하는 걸 의미, 이는 비용이 큼
# (이게 중요), 자원 소비 가능성이 증가 됨.
# *이러한 컨텍스트 스위칭 비용이 크기 때문에 멀티보다 싱글이 더 빠를 수 있음.


# yield, send  : 메인과 서브와 상호작용을 한다.
# 코루틴 제어, 상태, 양방향 전송
# 서브루틴 : 메인루틴 호출 -> 서브루틴에서수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소 -> 운영체제에게 많은 스레드가 필요해하지 않아도됨


# 코루틴 Ex1

def coroutine1() :
    print('>>> coroutine started.')
    i = yield # i에 yield 를 할당
    print('>>> coroutine received : {}'.format(i))

# 코루틴은 제너레이트에서 파생되었기 때문에 제네레이터 기반 코루틴이라고 설명하는 것이 있다.
# 함수와 제너레이트, 코루틴 등은 모두 def 로 만든다.
# 그래서 단순히 함수로 생각하지말고 안의 내용물을 확인해야 한다.

# 메인 루틴 ( 함수를 선언하므로 )
# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)
#next(cr1) # 끝이므로 에러발생,(for문에선 이런에러안나옴)

# 지금까지는 next로 데이터를 받기만 했지만 이제는 sub 루틴으로
# 데이터를 교환할 수도 있다.
# 코루틴이 100을 받았다고 나옴, 즉 send는 next의 역할도 함
# 처음 실행하면 위함수의 yield를 받은 i에 멈춰있다가 
# 메인 루틴에서100을넘겼고 서브루틴에서 받아서 i에 100을 할당한다음에
# yield 키워드 있을때까지 전진하나, 뒤에 더이상 없으므로 print되고 에러를 뱉는다.
# cr1.send() 이면 None이 전달됨.
# 값 전송
# cr1.send(100)

# 즉 메인루틴에서 서브루틴으로 수행을 하지만 이제는 send 함수로 메인과 서브가 데이터 교환이 가능하다는 것이다.
# 그래서 서로의 상태값을 교환한다.
# 만약 print('>>> coroutine received : {}'.format(i)) 에서 나 50% 밖에 일안끝났어 이러면
# 다시 send()를 줘서 얼마나 끝났는지 물어보면 100% 끝났어 라고 리턴되면
# '아 그럼 coroutine1은 일이 다끝났으니 다른일을 해도되겠구나' 하고 동시성 프로그래밍을 할 수 있게된다.



## 잘못된 사용
# next() 가 중간에호출이 안된상태
# -> 즉, 현재 i = yield 상태가아닌 상태
# 에서 send를 보내면 can't send non-None value ~ 예외가 발생한다.
cr2 = coroutine1()

#cr2.send(100)

# 파이썬의 코루틴
# GEN_CREATED : 처음 대기상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태 <-이때 send로 보내고 받을 수 있음
# GEN_CLOSED : 실행 완료 상태

# 처음에는 x를 메인루틴에서 받아서 서브루틴으로 전달함.
# x를 메인루틴에서 받아서 출력하고 
# y를 메인루틴에서 받아서 출력을 하는데 이때 x를 서브루틴에서 메인루틴으로 전달함
# 
def coroutine2(x) :
    print('>>> coroutine stated : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    # 서브루틴에서 나한테 준거 : x+y => print(send(값)) 해야 보임
    # 메인루틴에서 서브루틴으로 넘긴것 : z,
    z = yield x + y 
    print('>>> coroutine received : {}'.format(z))
    

cr3 = coroutine2(10)
#print(next(cr3)) # x에 10이 대입되고 print 됨, 현재는 y값을 받는 대기상태임
#cr3.send(100) # y값에 x가 대입되고 y가 print 됨
#cr3.send(100) # z값에 x+y가 대입되고 z가 print 됨, 더이상 yield없으므로 StopIteration 예외발생

# 상태값을 확인해 보겠다.
from inspect import getgeneratorstate

print(getgeneratorstate(cr3)) # GEN_CREATED
print(next(cr3))
print(getgeneratorstate(cr3)) # GEN_SUSPENDED

print(cr3.send(100))

print()
print()

# 파이썬 3.5이상에서 def -> async, yield -> await 으로 키워드로 바꿔쓸수있다.
# -> def로 같이 쓰면 혼돈이 되기 때문!

# 코루틴 Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리 (핵심적인 내용)

def generator1() :
    for x in 'AB' :
        yield x # A와B 둘다 받으려면 yield 2번필요
    for y in range(1,4) :
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()
# 제네레이트기 때문에 list로 형변환하면
# 알아서 list로 형변환 되면서 리스트가 만들어짐
# 이런 range같은 것들이 이렇게 반환이 된다는 걸 알 수 있을 것이다.
print(list(t2)) 

print()
print()

# generator1와 같은 로직이나 for문없이 yield from 으로 작성 
def generator2() :
    # yield : 이터레이블 한 데이터를 순차적으로, from : 끝날때까지 반환을하겠다.
    yield from 'AB'
    yield from range(1,4)
    
t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))   

print()
print()

# 정리하자면 많은 수의 함수를 코루틴을 이용하여 흐름제어를 할 수 있게된다.
# 함수1번실행->멈춤->함수 2번실행->멈춤->함수1번 다시실행 과 같이
# 그렇기 때문에 맨위에서 언급한것처럼 코루틴은 루틴의 실행 중 중지를 이용한 동시성 프로그래밍인 것이다.

