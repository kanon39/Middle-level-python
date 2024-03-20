# 가상환경에 asyncio와 beautifulsoup4 설치

# AsyncIO : 코루틴의 확장 버전.
# 비동기 I/O (Input, Output)작업을 쉽게 할 수 있도록 만듦.
# Generator -> 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# AsyncIO는 성능이 좋고 웹서비스, 클로링, DB 작업을 큐 기반으로 동작한다.

# 용어 설명 : Blocking I/O
# > 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음.
# > 그래서 타 함수는 대기

# 용어 설명 : NonBlocking I/O
# > 호출된 함수(서브루틴)가 Return 후 호출한 함수(메인 루틴)에 제어권 전달
# > 타 함수는 일 지속

# AysncIO를 써도 만약 내가 사용하려는 함수가 블럭 함수이면,
# AysncIO보다 단일 스레드로 만드는게 훨씬 빠르다.
# 따라서 내가 사용하려는 함수도 제네레이터와 같이 비동기로 구현되어야된다.
# 이를 우회하는 수준있는 예제를 이번에 다뤄보겠다.

# 쓰레드 단점 : 디버깅의 어려움, 자원 접근시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요없음 -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현이 되어 있어야 하거나 직접 비동기로 구현해야 함.

import asyncio
import timeit
from urllib.request import urlopen
# urlopen 은 블록함수이므로 AsynicIO로 구현하는 효과가 크지 않음.
# 따라서 이런 경우 코루틴의 스레드와 프로세스를 결합하여 많이 사용함.
# https://pymotw.com/3/asyncio/executors.html
# 스레드나 프로세스를 할 때 각각의 웹서버로 크롤링을 요청을 해도
# 각각의 스레드에서 하는 것이기 때문에 NonBlock(논블럭)의 효과를 받을 수 있다.
# 그때 코루틴으로 AsyncIO를 활용한다면 제대로 된 비동기의 효과를 볼 수 있다.

# 파이썬 AI 학습, 데이터 분석을 위해 데이터를 크롤링하거나
# 여러 작업을 한다고하면 실시간 이슈 등을 모아서 분석을 한다고하면
# 자동화된 파이썬 코드가 필요할 것이다.
# 여러 사이트에서 크롤링을 한다면 좀 더 빠르게 될 것이다.

from concurrent.futures import ThreadPoolExecutor 
import threading


# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예:게시판성 커뮤니티)

urls =['http://daum.net','https://naver.com','http://mlbpark.donga.com','https://tistory.com','https://wemakeprice.com']

# 동시에 실행을 하는데 문제가 뭐냐면 urlopen은 블록이므로 이를 쓰레드를 사용해서 따로 사용해준다면
# asyncio를 사용해서 코딩을 해볼 예정이다.

# 이 main 함수에서 쓰레드에서 asyncio로 넘기는 함수를 작성해보겠다.
# async 를 붙여서 비동기 함수라고 지칭한다.
# asyncio IO의 패턴이 있다. 이 패턴대로 개발을하면된다. (개발 순서1~)

# 개발 순서 3
async def fetch(url, executor) :
    # 쓰레드명 출력(쓰레드가 일을 잘하고 있는지 확인)
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    # 아래 loop는 main영역에서 생성을 했기 때문에 참조가능하다.
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    # 각 결과의 메인페이지에 대한 내용이 다 담겨 나올 것이다.
    # 이러면 모든 내용이라 디버깅이 쉽지 않으므로 각 사이트의 5글자만 가져오자.
    # 실행할때마다 start와 done 홈페이지 url 순서가 다르다. 이는 요청하고 보는 비동기를 의미한다.
    return res.read()[0:5]

# 개발 순서 2
async def main() :
    # 쓰레드 풀 생성
    # 쓰레드는 앞서 말한대로 urlopen 때문에 사용한 것이다.
    executor = ThreadPoolExecutor(max_workers=10) # 이렇게 worker 수를 정할수 있다.
    
    # future 객체 모아서 gather에서 실행
    futures = [
         # 아래가 중요. 여기다 실행할 함수들을 쌍으로 넣어줌
         # url 하나당 하나의 쓰레드, 각각의 쓰레드에서 각 싸이트 작업이 이루어진다.
         # 이를 urls 갯수 만큼 list comprehention이 된다.
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    # futures가 끝날때까지 기다린다.
    # futures가 리스트이기 때문에 언패킹을 해준다.
    rst = await asyncio.gather(*futures) # gather에서 최종적으로 기다렸다가 모아준다.
    
    print()
    print()
    print('Result : ', rst) # gather된 결과 출력

# 개발 순서 1
if __name__ == '__main__' :
    # 루프 초기화
    loop = asyncio.get_event_loop() # 제어권을 넘겨 받고, 주고 핑퐁하겠다.
    # 작업 완료 까지 대기
    loop.run_until_complete(main()) # 끝날 때 까지 이 루프는 계속된다.
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)
    
