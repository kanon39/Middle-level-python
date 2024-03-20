# 17강과 예제 동일
# 지금까지 단순히 프로세스와 스레드 두개로 실행을 해봤다면
# 동시성 처리를 응용할 수도 있다.
# 이때 가장 많이 사용되는 wait과 as_completed 가 있다.


# concurrent.map
# concurrent.wait, as_completed


import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

# 만약에 크롤링하는 예제라고 하면 A사이트, B사이트라고하면
# 각각 동일한 시간이 걸린다고 볼 수 없다.
# 이런 세세한 작업흐름을 컨트롤 해야된다.
# 한시간이 걸린다고 나머지 3개가 대기한다면 이런 것들에 대한 제한을 걸수있는
# wait 또는 as_competed 같은 메소드가 있다. 
# 또한 모두 성공한다는 보장또한 없다. 2개성공 2개 실패할 수도 있다.
# 이런 값들을 확인할 수 있어야 진정한 동시성 처리할 준비가 될 수 있다 볼 수있다.
WORK_LIST = [100, 1000, 10000, 2000000]

# 순차적으로 처리한다면 만구하고, 십만, 백만, 천만을 구해야하나
# 동시에 worker를 해서 각각 실행시켜 보겠다.
# 여기에 우리가 만든 함수를 리스트에 넣고 응용해도 된다.

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제레네이터)
def sum_generator(n) :
    return sum( n for n in range (1, n+1))
# 이 함수가 동시에 4개가 실행이 된다.
# worker :
# 작업자로는 스레드를 활용할 수도있고
# CPU의 프로세서를 활용할 수도 있다.

def main() :
    # Worker count 몇 명이서 일할 건데?
    # 몇명인지 모르면 OS에 맡겨도됨.
    # 리스트 작업 량에 따라 값지정, 최소 10개 이하
    worker = min(10, len(WORK_LIST))
    
    # 시작 시간
    start_tm = time.time() # 시작 시간
    
    # Futures 
    futures_list = []
    
    # 결과 건수
    with ProcessPoolExecutor() as excutor : #별칭 달기
        # 이 map은 작업이 다 끝날때까지기다렸다가 리스트형태로 결과들을 저장함.
        # 따라서 1시간이 걸리는 얘가  있다면 그냥 계속 기다림.
        for work in WORK_LIST :
            # submit은 미래에 할일만 반환함
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()
            
        # # wait 결과 값 출력
        # result = wait(futures_list, timeout=7) # 7초까지만기다려주고 7초가 넘으면 실패로 간주한다.(그래도 계속 실행됨.)
        # # 실행 후 7초 내 성공 한것만 보겠다.
        # print('Completed Tasks : '+str(result.done)) # done이 끝났는지
        # # 실행 후 7초 내 실패 한것만 보겠다.
        # print('Pending ones after waiting for 7 seconds : '+str(result.not_done)) # done이 끝났는지
        # # wait 결과 값 출력
        # print([future.result() for future in result.done])
        
        # # as_completed 결과출력
        # wait과 결과는 같지만,as_completed은 먼저 출력하는게 나온다는게, wait이 타임아웃을 줄 수 있다는 점이 다르다.
        for future in as_completed(futures_list) :
            result = future.result(all)
            done = future.done() # 잘 끝난 것 출력
            cancelled = future.cancelled # 취소가됬는지
            
            # future 결과확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))
        
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포맷
    msg = '\n Time : {:.2f}s'    
    # 최종 결과출력
    print(msg.format(end_tm))

# 지금까지는 실행을 그냥했지만
# 이제는 main 함수의 진입점을 알려줘야 됨

if __name__ =='__main__' : # 시작점을 명시적으로 작성 안그러면 멀티프로세싱 작업시 실행 안됨.
   main()
   
   
# 작업이 양이 작거나, 여유있게 일정 시간 이후 처리된데이터를
# 데이터베이스에 올릴 때는 wait으로 처리하고

# 빨리빨리 끝나는대로 다른 작업을 해야 되는 경우,
# 하나라도 끝난 데이터로도 일을 바로 할수있는 경우 as_completed을 쓴다.
# 공식 레퍼런스 future 함수에 모듈 함수의 딱 이 2개가 있다. 꼭 기억하자.

# 데이터 수집을 할 때 이를 이용하면 센스있고 빠르게 처리가 가능하다.
