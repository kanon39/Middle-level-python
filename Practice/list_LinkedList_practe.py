# 노드 구성
# value와 다음 노드의 메모리주소(next) 값을 가짐

class Node(object):
    def __init__ (self, value, next=None) :
        self._value = value
        self._next = next
    
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)

N1.next = N2
N2.next = N3

# 기본적인 LinkedList
class LinkedList(object) :
    def __init__ (self):
        # 여기서 head는 node 그 자체를 가르킴.
        self._head = None
    
    # LinkedList를 이용한 append 구현
    # append는 끝자리에 숫자가 와야함.
    def append (self,value) :
        new_node = Node(value)
        if self._head == None :
            self._head == new_node
        else :
            current = self._head
            while (current.next) :
                current = current.next
            new_node = current

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
    