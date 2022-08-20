class ListNode:
    def __init__(self, val=0, next=None):           
        self.val = val
        self.next = next

class MyCircularDeque:
    def __init__(self, k):                              # 생성자
        self.size = k                                   # k: 데크 사이즈
        self.contain = 0                                # contain: 아이템 개수
        self.forward = ListNode(None)                   # 정방향 연결 리스트
        self.backward = ListNode(None)                  # 역방향 연결 리스트
        self.head = self.forward                        # head 포인터
        self.tail = self.backward                       # tail 포인터

    def insertFront(self, val):                         # 데크의 앞쪽에 아이템 추가하는 메서드
        if self.contain != self.size:                   # 아직 데크 공간이 남아있을 경우에만 아이템 추가
            if self.contain == 0:                       # 빈 데크에서 처음으로 아이템이 추가될 경우
                self.forward = ListNode(val)            # foward와 head 자체를 추가된 연결 리스트로 설정
                self.head = self.forward

                self.backward = ListNode(val)           # backward와 tail 자체를 추가된 연결 리스트로 설정
                self.tail = self.backward
            else:                                       # 빈 데크가 아닌 상태에서 아이템을 추가할 경우
                temp_forward = ListNode(val)            # 임시 노드 생성
                temp_forward.next = self.head           # 임시 노드의 next를 self.head로 지정
                self.head = temp_forward                # self.head를 temp_forward로 지정
            
                self.backward.next = ListNode(val)      # backward.next를 추가된 아이템으로 지정
                self.backward = self.backward.next      # backward를 next로 이동시키기
                
            self.contain += 1                           # 아이템 개수 + 1
            return True  
    
    def insertLast(self, val):                          # 데크의 뒤쪽에 아이템 추가하는 메서드
        if self.contain != self.size:                   
            if self.contain == 0:
                self.forward = ListNode(val)
                self.head = self.forward

                self.backward = ListNode(val)
                self.tail = self.backward
            else:
                self.forward.next = ListNode(val)
                self.forward = self.forward.next

                temp_backward = ListNode(val)
                temp_backward.next = self.tail
                self.tail = temp_backward

            self.contain += 1
            return True
    
    def deleteFront(self):                              # 맨 앞의 아이템 삭제하는 메서드
        if self.contain != 0:                           # 데크에 아이템이 있을 때만 기능
            if self.contain == 1:                       # 데크에 아이템이 1개만 있을 경우
                self.forward = ListNode(None)           # 정방향 연결 리스트 초기화
                self.backward = ListNode(None)          # 역방향 연결 리스트 초기화
                self.head = self.forward                # head 포인터 초기화
                self.tail = self.backward               # tail 포인터 초기화
            else:                                       # 데크에 아이템이 2개 이상일 경우
                self.head = self.head.next              # head를 next로 옮김으로써 사실상 첫 번째 아이템 삭제
                
                temp_backward = self.tail               # 임시 노드 생성
                for _ in range(self.contain-2):         # backward 기준 마지막에서 두 번째 노드로 이동
                    temp_backward = temp_backward.next
                temp_backward.next = None               # next를 None으로 지정하여 마지막 아이템 삭제
                self.backward = temp_backward

            self.contain -= 1                           # 아이템이 하나 삭제되었으니 -1
            return True

    def deleteLast(self):                               # 맨 뒤의 아이템 삭제하는 메서드
        if self.contain != 0:
            if self.contain == 1:
                self.backward = ListNode(None)  
                self.forward = ListNode(None)   
                self.head = self.forward    
                self.tail = self.backward   
            else:
                self.tail = self.tail.next

                temp_forward = self.head
                for _ in range(self.contain-2):
                    temp_forward = temp_forward.next
                temp_forward.next = None
                self.forward = temp_forward

            self.contain -= 1
            return True
    
    def getFront(self):                                 # 첫 번째 아이템 출력하는 메서드
        if self.contain == 0:
            return -1
        else:
            return self.head.val
    
    def getRear(self):                                  # 마지막 아이템 출력하는 메서드
        if self.contain == 0:
            return -1
        else:
            return self.tail.val
    
    def isEmpty(self):                                  # 데크가 비었는지 확인하는 메서드
        return True if self.contain == 0 else False
    
    def isFull(self):                                   # 데크가 가득차있는지 확인하는 메서드
        return True if self.contain == self.size else False


if __name__ == '__main__':                              # 테스트
    d = MyCircularDeque(5)
    print(d.isEmpty())      # True
    d.insertFront(1)        # [1]
    d.insertFront(2)        # [2 1]
    d.insertLast(4)         # [2 1 4]
    d.insertLast(3)         # [2 1 4 3]
    d.deleteFront()         # [1 4 3]
    d.deleteLast()          # [1 4]
    print(d.getFront())     # 1
    print(d.getRear())      # 4
    d.insertLast(5)         # [1 4 5] 
    d.insertFront(7)        # [7 1 4 5]
    d.insertFront(8)        # [8 7 1 4 5] 
    print(d.isFull())       # True

        
        



