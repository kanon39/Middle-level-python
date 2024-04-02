
# 앞에서 DynamicArray는 기존 파이썬의 list으로 구성되어 있다.
# Node는 value와 Next address를 갖는다.

# class로 Node를 구현하면 이렇게 노드를 생성할 때 
# Value값과 Next 값을 초기화를 해줍니다.

# 어떤 값도 들어가지않으면 value는 0으로,
# next address는 None으로 초기화함.
class Node :
    def __init__(self, value=0, next = None) :
        self.value = value
        self.next = next
        

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



