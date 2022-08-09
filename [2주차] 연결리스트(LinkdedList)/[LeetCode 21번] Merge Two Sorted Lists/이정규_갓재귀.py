# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if (not list1) or (list2 and list1.val > list2.val) :
            list1, list2 = list2, list1 #작은 밸류값의 노드를 선정해 보다 앞 노드로
        if list1 : #list1에 노드가 남아있다면, 다시 한 번 작은 밸류값의 노드 선정
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


        