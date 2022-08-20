class ListNode:
    def __init__(self, val=0, next=None):           
        self.val = val
        self.next = next
        self.duplicate = 0

class BinaryHeap:                                               # 이진 힙 클래스
    def __init__(self):                                         # 생성자 메서드
        self.head = ListNode(None)                              # None값이 들어 있는 ListNode 인스턴스 생성

    def heap_push(self, new_node: ListNode):                    # heap_push 메서드
        if not self.head.next:                                  # ListNode가 비어있는 경우
            self.head.next = new_node
        else:                                                   # ListNode가 비어있지 않을 경우
            if new_node != None:                                # new_node가 None이면 수행하지 않음
                node = self.head                                # 기존 리스트를 옮겨다닐 node 정의
                while True:
                    if node.next != None:                       # node.next가 존재할 경우
                        if node.next.val >= new_node.val:       # 기존 리스트의 다음 노드가 새로운 리스트의 현재 노드보다 크거나 같을 경우
                            temp_node = node.next               # node.next를 temp_node로 받음
                            temp_new_node = new_node            # new_node를 temp_new_node로 받고 new_node는 next로 넘어감
                            new_node = new_node.next

                            node.next = temp_new_node           # node.next를 temp_new_node로 지정하고 temp_new_node.next는 temp_node,
                            temp_new_node.next = temp_node      # 즉 기존 노드(node)의 next지점으로 지정 -> 기존 노드 사이에 new_node.val이 들어옴

                        elif node.next.val < new_node.val:      # 기존 리스트의 다음 노드보다 새로운 리스트의 현재 노드가 클 경우
                            node = node.next                    # node 넘어감

                        if not new_node:                        # 더 이상 new_node에 원소가 없을 경우 break
                            break
                    else:                                       # node.next가 None인 경우에는 node.next를 new_node의 남은 요소들로 지정
                        node.next = new_node                
                        break

                    
   
## test ##
if __name__ == '__main__':
    list1 = ListNode(1)
    head1 = list1
    list1.next = ListNode(4)
    list1 = list1.next
    list1.next = ListNode(5)
    list1 = list1.next

    list2 = ListNode(1)
    head2 = list2
    list2.next = ListNode(3)
    list2 = list2.next
    list2.next = ListNode(4)
    list2 = list2.next

    list3 = ListNode(2)
    head3 = list3
    list3.next = ListNode(6)
    list3 = list3.next

    # list1 = ListNode(2)
    # head1 = list1
    # list2 = None
    # head2 = list2
    # list3 = ListNode(-1)
    # head3 = list3

    bh = BinaryHeap()
    bh.heap_push(head1)
    bh.heap_push(head2)
    bh.heap_push(head3)

    bh.head = bh.head.next
    while bh.head:
        print(bh.head.val)
        bh.head = bh.head.next