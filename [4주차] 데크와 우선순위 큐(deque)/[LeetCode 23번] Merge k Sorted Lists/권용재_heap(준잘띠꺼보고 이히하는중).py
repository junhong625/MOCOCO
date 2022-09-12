class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        
        heap = []
        for l in lists:                                 # 연결리스트의 원소를 heap리스트 에 모두 저장
            while l:
                heap.append(l.val)
                l = l.next
        heapq.heapify(heap)                             # heap리스트를 heap자료구조로 변환 ---> 여기사 왜 ???
        
        head = tail = ListNode()                        # head와 tail 생성
        
        for _ in range(len(heap)):
            tail.next = ListNode(heapq.heappop(heap))   #뒤에다 계속 남아있는 최소값을 붙여주면서 연결 리스트 이어줌.
            tail = tail.next
        
        return head.next
