# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, addup = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = result = ListNode() # root.val = result 이기에 result에 담기는 모든 조건은 root에서도 적용된다!!
        # 조건들을 전부 if로 설정하였으나, 결과적으로 어떠한 이유에선지 모든 조건을 만족시키지 못하였다.
        # 따라서 이러한 조건을 버리고, 그냥 책을 참고해서 while문을 적용시켜보았다.
        # if l1 == None and l2 == None:
        #     return None
        # elif l1 == None:
        #     l1 = ListNode(addup,None)
        # elif l2 == None:
        #     l2 = ListNode(addup,None)
        # elif l1 == 0 and l2 == 0:
        #     return 0
        # elif l1 == 0:
        #     return l2
        # elif l2 == 0:
        #     return l1
        while l1 or l2 or addup:
            new3 = addup
            if l1:
                new3 += l1.val
                l1 = l1.next
            if l2 :
                new3 += l2.val
                l2 = l2.next

            if new3 >= 10:
                new3 = new3 - 10
                addup = 1
            else :
                addup = 0
            result.next = ListNode(new3)
            result = result.next
        return root.next