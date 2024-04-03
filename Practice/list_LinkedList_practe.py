# 노드 구성
# value와 다음 노드의 메모리주소(next) 값을 가짐

class Node () :
    def __init__ (self, value=0, next=None) :
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
# 기본적인 LinkedList
# Linked List 는 여러개의 노드가 연결되어 있고
# Linked 된 노드들을 접근할 때 head의 노드로 접근해야 됨.

# 이때 append를 구현해보자. append는 두개의 커서가 있어야 됨.
# 맨처음 노드를 가르키는 head 커서 하나, append될 값이 위치할 list 끝자리 커서하나.
class LinkedList ():
    def __init__ (self) :
        self.head = None
        
    def append (self, value) :
        # 위의 head가 더이상 메모리 None을 가르키지 않고 new_node를
        # 가르킬 수 있도록 new_node = Node(value)
        new_node = Node(value)
        try :
            print('첫번째 head 값 : ',self.head.value)
        except AttributeError :
            print('head 값은 None')
        
        if self.head == None :
            self.head = new_node
            # head는 init에 있고 class내에서 공유되므로
            # append가 한번실행될때 head에 변화가 발생한다면
            # 두번 실행될때 head의 변화 내용이 그대로 옮겨감.
            # 우리가 지정한 current에 self.head 내용을 넣는다.
        else :
            current = self.head 
            while (current.next) :
                current = current.next
            current = new_node
            print('current 값 : ',current.value)
            
test = LinkedList()
a = test.append(1)
a = test.append(2)
a = test.append(3)
