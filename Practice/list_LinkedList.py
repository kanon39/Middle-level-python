
# 앞에서 DynamicArray는 기존 파이썬의 list으로 구성되어 있다.
# Node는 value와 Next address를 갖는다.

# class로 Node를 구현하면 이렇게 노드를 생성할 때 
# Value값과 Next 값을 초기화를 해줍니다.

# 어떤 값도 들어가지않으면 value는 0으로,
# next address는 None으로 초기화함.
class Node :
    def __init__(self, value=0) :
        self.value = value
        self.next = None
        
        

first = Node(1)
second = Node(2)
third = Node(3)
# 이렇게 하면 Node들끼리 연결이 안되어 있다.
# 따라서 first의 next 값이 second를 가르켜라
# second도 third에 가르키게 해라.
first.next = second
second.next = third
# first.value를 6으로 업데이트 해줌
first.value = 6

# 지금까지 Node들을 구현해봤다.
# 그러나 우리가 만들고자 하는건 LinkedList.
# 단한가지 만족이 안됬는데,
# 여기서 Head가 첫 번째 linkedlist의 첫번째 노드 값을 가르켜야 된다.
# 헤드(head)가있다면 헤드를 통해서 첫번째 노드로갈 수도,
# 두번째 노드는 헤드를 통해서 첫번째 노드로 갔다가 Next address를타고
# 두번째노드를 갈 수 있고.. 

# linkedList의 가장 간단한 opeartion인 insert_back()(a.k.a append())
# 를 구현해 보겠다.

class LinkedList(object) :
    def __init__ (self) :
        self.head = None
        
    def append(self, value) :
        new_node = Node(value)
        self.head = new_node
# 이떄 새로운 new_node가 만들어질때마다 head는그 노드를 가르키게됨.
# 노드가 처음 생성될 때랑 그 다음부터는 기능 구현이다르겠구나.
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
        # 마지막 노드가 뉴 노드를 가리키게끔 바뀌어야 한다.
            current = self.head
            while (current.next) :
                # 마지막 Node가 여기 Next address를 new node를가리키게끔해야 한다.
                # 하지만 우린 head부터 시작해서 타고타고 마지막 노드로 간다음에 
                # 이 노드에 next address로 new node를 집어넣어야 함.
                # 따라서 current 변수 생성
                # 계속 타고타고 가야되므로 current.next가 NOne일때까지간다.
                current = current.next
            current.next = new_node
# 이렇게 node를구현하고 linkedList를 토대로 한 append 기능을 구현해보았음. 
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# 코드가 완벽하진않을것이지만, 어떤원리로 append가 되었는지, 이해한다면
# 다른 오퍼레이션들을 다 구현할 수 있을 것이다.
# 코드는 상황과 사람에 따라서 항상 바뀔수밖에없을 것이다. 


# Linked List에는 다음의 것들이 있다.
# 특정 인덱스에 저장되어 있는 값들을 반환하는 get operation,
# 파이썬 append 와 같은 insert_back
# append와 달리 앞에추가하는 insert_front
# 링크드리스트 중간에 데이터 삽입하는 insert_at
# 데이터를 추가했으면 삭제하는 것도 있으므로 remove_back
# remove_front()
# remove_at
# ....

# 이중 배울 내용이 많은 오퍼레이션을 선별해서 구현해 보겠다.
 
# get 오퍼레이션
# 몇번째 입력값을 받아야 되므로 idx를 인수로 추가한다.

class LinkedList() :
    def __init__ (self) :
        self.head = None
        
    def append(self, value) : # 앞에서 구현 -> 시간복잡도도 O(n) 임.
        new_node = Node(value)
        self.head = new_node
        if self.head is None :
            self.head = new_node
        else :
            current = self.head
            while (current.next) :
               current = current.next
            current.next = new_node
            
    def get(self, idx) :
        # linkedList에서 특정 인덱스에 저장되어 있는 값을 알려면
        # 일단 그 값까지 가야된다.
        # arrayList 처럼 랜덤 엑세스가 되는게 아니기 때문에
        # current를 한칸씩, 한칸씩, 한칸씩 움직여야 그곳에 저장돼 있는 value를 리턴할 수 있다.
        # 만약 array라면 시간복잡도가 O(1)으로 원하는 인덱스에 갈 수 있을텐데
        # 링크트리스트로 가려면 무조건 head를 통해서 가고 인덱스 수만큼 시간복잡도가 늘어나므로
        # 링크드 리스트의 시간복잡도는 O(n)이다.
        
        # Task 1. head에 접근
        # Task 2. 원하는 index로 이동
        # Task 3. value 반환
        # 첫시도 - 실패 (append가 앞서 진행되어 이미 self.head가 끝 값을 가르키고있음.)
        # current = self.head
        # n = 1
        # if idx == 0 :
        #     return current.value
        # elif idx > 0 :    
        #     while n == (idx) :
        #         current = current.next
        #         n += 1
        #     return current.value
        current = self.head
        for _ in range(idx) :
            current = current.next
        return current.value
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.get(1)) # 첫시도 실패이유와 동일하여 원하는 자릿수 출력 불가.