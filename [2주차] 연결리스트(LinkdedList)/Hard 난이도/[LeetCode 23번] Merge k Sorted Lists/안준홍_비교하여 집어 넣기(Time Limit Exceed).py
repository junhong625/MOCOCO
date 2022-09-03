# 정답은 출력하지만 시간이 오래 걸려 Time Limit Exceed에 걸려버렸다!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # 기준점을 잡을 연결리스트를 고르기 위한 반복문
        for l in range(len(lists)):
            # 연결리스트가 비어있지 않을 경우 해당 연결리스트를 기준점으로 설정
            if lists[l] != None:
                result = lists[l]
                break
        else:
            return
                
        # 기준점인 연결리스트의 다음 순번 부터 하나씩 꺼내 비교
        for l_list in lists[l+1:]:
            # 기준점 연결리스트의 헤드 복사
            dummy = result
            # 비교 연결리스트의 끝까지 반복
            while l_list:
                # 비교 연결리스트의 현재 값과 기준 점 연결리스트의 현재 값을 비교하여 비교 연결리스트가 더 작을 경우
                if l_list.val < dummy.val:
                    # 비교 연결리스트 값의 다음 포인터로 기준점 연결리스트를 가리키는 새로운 연결리스트를 생성하여 기준점으로 변경 
                    result = dummy = ListNode(l_list.val, dummy)
                    l_list = l_list.next
                    continue
                # 기준점 연결리스트의 끝까지 갔음에도 비교 연결리스트 보다 작은 값이 없다면 기준점 연결리스트의 끝에 추가
                if dummy.next == None:
                        dummy.next = l_list
                        break
                # 비교 연결리스트의 값이 기준점 연결리스트의 현재 값과 다음 값 사이일 때
                if l_list.val in range(dummy.val, dummy.next.val):
                    # 다음 포인터의 메모리 주소를 미리 복사
                    next = dummy.next
                    # 기준점 연결리스트의 다음 포인터를 새로 생성한 노드로 설정
                    # 미리 복사해둔 메모리 주소를 다음 포인터로 지정
                    dummy.next = ListNode(l_list.val, next)
                    l_list = l_list.next
                dummy = dummy.next
        return result
    
