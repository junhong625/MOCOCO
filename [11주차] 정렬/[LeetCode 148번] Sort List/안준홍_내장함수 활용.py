class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_list = []                             # 문자가 들어갈 리스트
        while head:                             # head가 존재할 경우 반복
            s_list.append(head.val)             # s_list에 각 노드의 값을
            head = head.next                    # 다음 노드로 이동
        s_list.sort(reverse=True)               # 거꾸로 정렬
        
        head = root = ListNode()                # 정렬된 노드들이 들어갈 연결리스트
        while s_list:                           # s_list가 존재할 경우 반복
            head.next = ListNode(s_list.pop())  # 현재 노드의 다음 노드에 s_list의 마지막 값을 추출하여 추가(거꾸로 정렬했기에 마지막 값이 제일 작은 값)
            head = head.next                    # 다음 노드로 이동
        return root.next                        # 시작지점의 value가 None이기에 next값부터 출력