# 노드 구성
# value와 다음 노드의 메모리주소(next) 값을 가짐

class Node () :
    def __init__ (self, value=0, next=None) :
        self.value = value
        self.next = next


# first = Node(1)
# second = Node(2)
# third = Node(3)
# first.next = second
# second.next = third
# 기본적인 LinkedList
# Linked List 는 여러개의 노드가 연결되어 있고
# Linked 된 노드들을 접근할 때 head의 노드로 접근해야 됨.

# 이때 append를 구현해보자. append는 두개의 커서가 있어야 됨.
# 맨처음 노드를 가르키는 head 커서 하나, append될 값이 위치할 list 끝자리 커서하나.
class Node () :
     def __init__ (self, value=0, next=None) :
         self.value = value # 특정값
         self.next = next # 특정값 다음에 이어지는 노드의 메모리주소값 저장

class LinkedList ():
    def __init__ (self) :
        self.head = None
        
    def append (self, value) : # O(n)
        # 위의 head가 더이상 메모리 None을 가르키지 않고 new_node를
        # 가르킬 수 있도록 new_node = Node(value)
        new_node = Node(value)
        #try :
        #    print('첫번째 head 값 : ',self.head.value)
        #except AttributeError :
        #    print('head 값은 None')
        
        if self.head == None :
            # 첫지점 head 지정
            self.head = new_node
            # head는 init에 있고 class내에서 공유되므로
            # append가 한번실행될때 head에 변화가 발생한다면
            # 두번 실행될때 head의 변화 내용이 그대로 옮겨감.
            
        else :
            # 첫지점 head와  current 위치 일치 시키기
            current = self.head 
            while (current.next) :
                # while이 돌면서 매번 current 내 next를 업데이트 시킴
                # = current의 커서 이동
                # current의 끝지점 정보를 current에 저장
                current = current.next
            # current 끝지점에 새로운 노드 삽입 -> append 완료
            current.next = new_node
        
    def get (self, idx) :
        # 첫지점 head와  current 위치 일치 시키기
        current = self.head
        for _ in range(idx) :
            # 정해진 index만큼  current 내 next를 업데이트 시킴
            # = current의 커서 이동
            # current의 끝지점 정보를 current에 저장
            current = current.next
        # get은 호출이므로 current 내부의 value값을 return 해줌
        return current.value 
        
    
    def insert (self, idx, value) : # O(n)
        # 삽입예정인노드 생성
        new_node = Node(value)
        # 첫지점 head와  current 위치 일치 시키기
        current = self.head
        for _ in range(idx-1) :
            # 정해진 index만큼  current 내 next를 업데이트 시킴
            # = current의 커서 이동
            # current의 끝지점 정보를 current에 저장
            current = current.next
            print(current.value)
        pre = current.next
        current.next = new_node
        new_node.next = pre
        
        
    def remove (self, idx) :
        current = self.head 
        for _ in range(idx-1) :
            current = current.next
        
        pre = current # 이전 노드 저장
        current = current.next # 연결된 노드 이동
        pre.next = current.next # 이전노드에 연결된 노드 다음 노드 연결
        
        
    def print(self, idx = 0):
        print("====== Linked List ======")
        current = self.head
        while(current):
            if current.next is not None :
                str_value = str(current.value)
                str_next = str(current.next)[-12:-1]
            else :
                str_value = str(current.value)
                str_next = str(current.next)
            print(" Node(" + str_value + ")=", end='')
            print("(" + str_value + "," + str_next + ")")
            current = current.next
        print("=========================\n")
test = LinkedList()
test.append(1)
test.append(2)
test.append(3)
test.insert(1,5)
test.print()

test.remove(2)
test.print()
#print([ test.get(x) for x in range(4) ])
