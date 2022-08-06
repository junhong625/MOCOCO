# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        x = list1
        y = list2
        result = ListNode(0)
        while x or y:
            if x == None:
                result.next(y.val)
                break
            elif y == None:
                result.append(x.val)
                break
            elif x.val >= y.val:
                result.append(y.val)
                y = y.next
            elif x.val < y.val:
                result.append(x.val)
                x = x.next
        return result


            