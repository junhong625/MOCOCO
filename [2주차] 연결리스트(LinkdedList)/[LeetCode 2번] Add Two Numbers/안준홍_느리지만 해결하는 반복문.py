# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# l1을 l1과 l2의 val을 더한 값을 저장한 연결리스트로 만드는 함수 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # head와 같은 역할을 하는 result
        result = l1
        # 다음 자릴수에 더해질 수
        up = 0
        # l1과 l2중 더욱 짧은 연결리스트 길이 - 1 만큼 반복하며 l1.val에 up과 l2.val을 더하는 반복문
        while l1.next and l2.next:
            sum_val = l1.val + l2.val + up
            if sum_val >= 10:
                sum_val, up = int(str(sum_val)[1]), int(str(sum_val)[0])
            else:
                up = 0
            l1.val = sum_val
            l1 = l1.next
            l2 = l2.next
        # 탈출 후 짧은 연결리스트의 길이만큼 채우기 위해 l1.val에 up과 l2.val을 더해주기
        l1.val += l2.val + up
        # 다음 자릿수에 더해질 값을 설정하기 위한 조건문
        if l1.val >= 10:
                l1.val, up = int(str(l1.val)[1]), int(str(l1.val)[0])
        else:
            up = 0
        # l2의 다음 포인터가 아직 있을 경우 l1의 다음 포인터를 l2의 다음 포인터로 설정(l2의 다음 포인터가 있다는 것은 위 반복문에서 l1의 다음 값이 없어 탈출 했다는 것)
        if l2.next:
            l1.next = l2.next
        # 만약 올림 수가 있다면 반복
        while up == 1:
            # 올림 수가 있지만 l1의 다음 포인터가 없을 경우 다음 값을 새로운 Node로 설정하고 result를 반환
            if l1.next == None:
                l1.next = ListNode(up)
                return result
            # 올림 수가 있고 l1의 다음 포인터도 있을 경우 다음 포인터로 이동하여 해당 포인터의 값에 up을 더해줌
            l1 = l1.next
            l1.val += up
            # 다음 자리수에 더해질 up을 설정하기 위한 조건문
            if l1.val >= 10:
                l1.val, up = int(str(l1.val)[1]), int(str(l1.val)[0])
            else:
                up = 0
        
        return result
            