# 오늘은 context manager annotation을 이용해서
# class 형태가아닌 함수형태로 구성해보겠다.

"""
Chapter 2
python Advanced(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__

"""
"""
가장 대표적인 with 구문 이해
contextlib 데코레이터 사용
코드 직관적, 예외 처리 용이성
코드는 개발자들끼리의 대화다.
"""
import contextlib
import time



# Ex1
# Use decorator

# 아래 contextlib.contextmanager를 보면
# 자원 할당과 회수를 담당하는 __enter__(또는 yield)와 __exit__구문이있겠구나라고 생각할 수 있음
@contextlib.contextmanager 
def my_file_writer(file_name, method) :
    f = open(file_name, method)
    # 한번에 메모리에 풀로올리는게 아니라 하나하나 원소를반환하고
    # 다음의 위치를 기억하는 역할을 하는 yield 이게 바로
    # __enter__ 구문에 해당
    yield f # __enter__
    f.close() # __exit__ 이부분에서 예외처리를 하면 되겠구나라고 판단가능

# 만약 예외처리를 FM대로 제대로 하겠다 라고하면 class로 작성하고
# 그게 아니라면 function 형태로 작성한다.

with my_file_writer('testfile4.txt','w') as f :
    f.write('Context Manager Test4.\nContextlib Test4')

# Ex2
# Use decorator
# 예외처리 포함

@contextlib.contextmanager
def ExcuteTimerDc(msg) :
    start = time.monotonic()
    try : # __enter__
        yield start
    except BaseException as e :
        print('Logging exception: {}:{}',format(msg,e))
        raise
    else : # __exit__
        print('{}:{}s'.format(msg, time.monotonic()-start))
        
with ExcuteTimerDc('Start Job1') as v :
    print('Received start monotonic2 : {}'.format(v))
    
    # Excute job.
    for i in range(10000000) :
        pass
    
    #raise ValueError('occurred.')
    
    