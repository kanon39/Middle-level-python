# 19강 예제를 좀 더 다르게 표현해보겠다.
# title의 내용을 다 가져와보겠다.
# 뷰티풀수프는 자주활용되는 패키지 5위정도에 공식 레퍼런스도 잘 정리되어 있다.


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
from bs4 import BeautifulSoup
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
#######################################################################
# asyncio IO의 패턴이 있다. 이 패턴대로 개발을하면된다. (개발 순서1~순서3)
# 이게 중요하다.
#######################################################################
# 개발 순서 3
# >>>>>>>>>>>>>>>> 19강과 다른 부분
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
    
    # 앱에서 가져올 데이터를 res.read()로 가져오고
    # html parser 해석기를 통해서 soup에 넣어준다.
    soup = BeautifulSoup(res.read(), 'html.parser')
    
    # 전체 페이지소스 확인
    # prettifuy를 하면 이쁘게 출력해줌
    # print(soup.prettify())
    # 우리가 필요로 하는 걸 가져오자.
    result_data = soup.title # 가져오고 싶은걸 가져오기
     
    return result_data

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
    
    

# 초반에는 파이썬은 쉽지만, Django 등 프레임워크를 다루게 되면
# 파이썬은 쉽다라고 하는 내용엔 공감을 못한다.
# 지금까지 어려운 과정이었고 중급 강의가 책으로만 보면 설명이 쉽지않고 딱딱하기 때문에
# 연강으로 설명했었다. 

# 완벽한건 없다 교류하면서 발전해야 함.

