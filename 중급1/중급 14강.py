# 파이썬 기초, 프로그래밍 개발을 할 때 한가지 미션을 어떻게 처리해야할지
# 지금까지 배운 것의 총망라하는 파트다.
# 코딩은 쉽지만 생각을 많이해야 한다.
# 방법을 생각하고 사고의 폭이 넓어지고 실력이 늘것이다.
# 파이썬에서 선언하는 모든것들을 class로 할 수 있다.

# 병행성 (Concurrency) 


# python Iterater와 generator : 
# generator : Iterater를 리턴한다. 반복가능한 개체를 생산해내는(리턴하는) 역할을 한다.
# Iterater : 반복 가능한 개체라는 것이다.

# 파이썬 반복 가능한 타입
# collections, text , list, Dict, Set,Tuple, unpacking한 요소들, *args ... : 얘네들은 모두 반복가능하기 때문에
# iterable 하다고 하고 이를 만들어내는게 iterator이다.

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# dir 해도 __iter__이 있다. 
print(dir(t))

# 반복가능한 이유? : 내부적으로 어떻게 실행됬냐면 t가 iter 함수를 호출해서 iterable을 받아서
# next라는 함수를 통해서 하나하나 실행이된것이다.
# 이를 하는 이유는 scope 일급함수를 배우고 클로저를 배웠다.
# 제너레이터와 이터레이터를 해야 병행성을 할 수 있기 때문.

for c in t:
    print(c)

# while 문으로 바꿔보기
w = iter(t)
print(dir(w)) # next 문이 있음

print(next(w)) # A 출력
print(next(w)) # B 출력
print(next(w)) # C 출력 > 실행될때마다 이전 값에 대한 위치정보를 가지고 있음

while True :
    try : 
        print(next(w)) # 위의 for문으로 했을 때와 같게나옴
    except StopIteration :
        break
print()

# 만약 while문으로 반복을해야된다고 문법을 설명한다면 예외처리, iter 함수 호출, next 호출하는게 불편하다.
# 따라서 for문이 아래 while문처럼 작동한다고 이해하면 된다.
# 직접 이 코드를 쓰진 않더라도 원리를 알면 된다.

# 반복형확인

from collections import abc # 상속을받았는지 확인하는 함수 True면 Iterator가 있단 얘기

#### iterator를 확인하는 3가지 방법 ####
print(dir(t))
print(isinstance(t, abc.Iterable)) # t가 추상클래스의 Iterator를 상속받았는지 본다. True면 Iterator가 있단 얘기 
print(hasattr(t, '__iter__')) # hasattr에서 True가 나오면 얘는 Iterator 라는 얘기다.

print()
print()

# 클래스기반 제너레이터 구현

# next 패턴
class WordSplitter :
    def __init__(self, text) : 
        self._idx = 0
        self._text = text.split(' ') # 공백기준
    
    def __next__(self) : # 넥스트 함수로 구현
        #print('Called __next__')
        try : # next가 호출될 때마다 다음 단어가 나옴
            word = self._text[self._idx] + '0'# 이와 같이 이터레이터에 패턴을 넣을수도있다.
        except IndexError :# 단어의인덱스에러가날떄까지
            raise StopIteration('Stopped Iteration. ^_^')
        self._idx += 1
        return word
    def __repr__ (self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorrw')
print(wi)
print(next(wi)) # 클래스지만 이터레이블 하게쓸수있다.
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
#print(next(wi))
# 하지만 next 패턴은 불편하다. 예외처리에 index +1도해야한다.

# 똑같은 예제를 이번엔 제너레이터 패턴으로 작성해보겠다.
# 제너레이터는 많은 장점을 가지고 있다. 
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가, 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator :
    def __init__(self, text) :
        self._text = text.split(' ')
    
    def __iter__(self) : # iter 함수를구현해주면 다음에 return된 위치값을 기억하게 된다.
        for word in self._text :
            # 제네리이터 , return도 없어도 됨, yield는 뒤에 나올 예정
            # iter함수에서 yield에서 "내부적으로" 다음에 반환될 값의 위치정보를 기억하게 된다.
            yield word 
        return
    def __repr__ (self):
        return 'WordSplitGenerator(%s)' % (self._text)
    
wg = WordSplitGenerator('Do today what you could do tommorrw')

wt = iter(wg)
print(wt, wg)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))


# 제네레이터에서 이터레이터로 반환해서 next로 순회를 할 수 있었다.
# class 에서도 iterable하게 만들어 봤다.
# 파이썬에서 내부적으로 사용하는 반복 ,순회에대해서 배웠으며
# yield 를 사용함으로써 index를 따로 작성하지 않고도 다음에 반환횓 값에 대한 위치정보를 기억하고 있다.
# 이 키워드가 나중에 코르틴이 된다.

print()
print()