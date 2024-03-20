# 앞전의 3개의 강의는 필수 문법을 배우는 복습과정이고
# 한번쯤 생소하거나 내가 사용할 일이있나..? 왜 이렇게 구현되는 건가?
# 라는 것들을 하나하나씩 배워보겠다.
# 첫번째로 context manager 이다.

# 언더바__ 양옆에 붙은것을 매직메서드라고하는데,
# 인스턴스가 초기화될때 파이썬의 정해진 규칙대로 호출되는 그런 형태의 메소드를 뜻함.

# Context manager를 잘하면 외부 리소스를 처리할때도 안전하게 처리하는
# 모듈화가 가능하다.

"""
Chapter 1
Python Advanced(1) - Context Manager(1)
keyword - Contextlib, __enter__, __exit__, exception

"""
# 운영체제 작업은 한정되어 있다.
# 문을열었음 문을 닫아야되고, 책을 도서관에빌렸으면 책을반납해야된다.
"""

1. 컨텍스트 매니저 
컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용 프로그램 개발 중요(문제 발생 요소)

요약 : 프로그램에서 어떤 데이터베이스 작업, 파일 I/O하거나, 웹 커넥션이 연결되는것은
한정된 자원에서 이루어지기 때문에 특정 상황에서 예외가발생, 에러가 발생할 수 있다.
이럴 때 자원관리를 엄격한 타이밍에 하기위해 파이썬에서는 with문을 사용한다.
하지만 우리는 with문의 메커니즘을 활용한 __enter__, __exit__ 클래스를 통해서
우리가 원하는 자원의 할당과 회수 뿐만 아니라 우리가 원하는 로직을 추가하고
또 class를 이용해서 우리가원하는 형태를 만들 수 있다는 것이다.

2. Contextlib - Measure execution(타이머) 제작


"""

# Ex1

file = open('./textfile1.txt', 'w')
try :
    file.write('Context Manger Test1 \nContextlib Test1.')
finally :
    file.close()
    
# 이렇게 try, finally로 쓰다가 나온 것이 with문이다.
# 이 with문은 위와다르게 close()를 하지 않아도 알아서 자원을 반환한다.
# 즉 이 with문이 내부에 설계되어있다.

# Ex2
with open('./textfile2.txt', 'w') as f :
    f.write('Context Manger Test1 \nContextlib Test2.')
    
# 우리는 이 with문을 커스텀해서 파일 뿐 아니라 인터넷 접속 하고 끊을 떄도
# 인터넷 접속하고 나올 때는 연결을 끊어, 실행 스타트 시간과 끝나는 시간을 계산한다등
# 따라서 다른사람들이 내코드를 읽거나 쓸때 리소스의 반환까지 신경쓰는게아니라
# 단지 앞에 with라는 예약어를 붙이고 우리들이 만들어 놓은 컨텍스트매니저에 들어와서
# 내가의도한대로 객체를 사용할 수 있게 된다. 

# Ex3
# with 문처럼 자원의 할당과 반환하는 코드를 직접 짜보겠다.
# use class -> context manager with exception handling
# 어떤 class 문 안에 enter와 exit가 있다면 context manager로 작동한다.
class MyFileWriter() :
    def __init__ (self, file_name, method) :
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
    
    # 진입했을 때 
    def __enter__(self) :
        print('MyFileWriter Started : __enter__')
        return self.file_obj
    
    # 나갈 때
    # __exit__는 인자가 3개로 고정되어있다.
    # __exit__(self, 예외발생시 예외 타입, 예외 값, 변수이름 )
    def __exit__(self, exc_type, value, trace_back) :
        print('MyFileWriter started : __exit__')
        if exc_type : # exc_type이 True이면 예외 발생할시 value와 trace_back 이 같이 넘어옴
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()
    
# 아래가 실행되면
# initializing이 될 것이고
# init 안에서 초기화해서 실행이 되서 에러가 될경우 exit의 if문이 실행이 된다.
# 위의 open 클래스도 마찬가지로 __enter__와 __exit__ 클래스가 구현이 될 것이다.
with MyFileWriter('./textfile3.txt', 'w') as f :
    # f에서 file_obj가 전달되어 write 함수 실행가능
    f.write('Context Manger Test1 \nContextlib Test3.')
    

## 타이머 클래스 ##
# 타이머 클래스를 개발해두면 어떤 함수에 넣으면 시간 측정 가능
# 예외 : 프로그램 적으로 발생, 예외처리를 해서 프로그램 흐름에 영향안받음
# 에러 : 물리적인 고장, 프로그램이 정상적으로 동작하지 않을 때 발생
import time

class ExcuteTimer() :
    def __init__ (self, msg) :
        self._msg = msg
        
    def __enter__(self) :
        #monotonic 함수는 시간을 숫자형태로 가져와서 _start에 저장
        self._start = time.monotonic() 
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback) :
        if exc_type :
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else :
            print('{} : {} s'.format(self._msg, time.monotonic()-self._start))
        return True # True로 하는건 __exit__를 잘 빠져나왔어요 라는 뜻이다.
    
with ExcuteTimer('Start! job') as v :
    print("Received start monotonic 1 : {}".format(v)) # v는 __enter__에서 _start가 넘어온다.
    # Excute job
    # 여기다가 직접만든 함수, 테스트하고 싶은 함수를 넣는다.
    # 아래 for문을 빠져나가면서 __exit__ 실행 되어
    # -> print('{} : {} s'.format(self._msg, time.monotonic()-self._start)) 실행됨.
    for i in range(100000) :
        pass


# 예외를 강제로 발생시키기
with ExcuteTimer('Start! job') as v :
    print("Received start monotonic 1 : {}".format(v)) # v는 __enter__에서 _start가 넘어온다.
    # Excute job
    # 여기다가 직접만든 함수, 테스트하고 싶은 함수를 넣는다.
    # 아래 for문을 빠져나가면서 __exit__ 실행 되어
    # -> print('{} : {} s'.format(self._msg, time.monotonic()-self._start)) 실행됨.
    for i in range(100000) :
        pass
    raise Exception('Raise!Exception!!') # 강제로 발생
