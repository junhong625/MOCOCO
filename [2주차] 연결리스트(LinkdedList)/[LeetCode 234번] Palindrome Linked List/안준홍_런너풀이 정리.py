# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def isPalindrome(self, head): 
        # rev에는 아무값도 저장되어 있지 않다.
        rev = None 
        # head의 데이터가 slow와 fast에 저장된다.
        slow = fast = head 

        # 런너를 이용해 역순 연결 리스트 구성
        # fast가 끝에 도달할 때 까지 루프
        while fast and fast.next: 
            # fast는 두칸씩 이동하고 slow는 한칸씩 이동하기에 fast가 끝에 도착하면 slow는 중앙에 도착
            fast = fast.next.next

            # 아래와 같은 3가지를 거쳐 각 데이터들이 이동 및 저장되는 변수
            # 1. rev.next에는 현재 rev값의 메모리 주소를 추가 -> 즉 rev.next를 하게되면 연결되어 있는 메모리주소로 이동 
            # - 루프를 돌아 마지막으로 rev값이 저장된 이후 rev.next를 하게되면 그전에 저장했던 값들을 가져올 수 있기에 역순으로 데이터를 꺼낼 수 있다. -> stack과 유사 LIFO구조 
            # 2. rev에는 slow의 메모리 주소를 추가
            # 3. slow는 slow.next에 저장되어 있는 메모리 주소로 이동 
            rev , rev.next , slow = slow, rev , slow.next 

        # 연결리스트의 길이가 짝수일 경우 fast는 위 루프를 돌아 데이터가 남아있지 않기(None)에 이 조건문을 건너뛰지만
        # 홀수일 경우 fast는 연결리스트의 마지막 값이 남아있다. 그렇기에 아래 조건문을 실행하고 slow는 중간값을 건너뛰어 정상적으로 palindrome인지 체크할 수 있게 된다. 
        if fast: 
            slow = slow.next 
        
        # palindrome 여부확인
        while rev and rev.val == slow.val: 
            slow, rev = slow.next , rev.next

        # palindrome 여부확인 루프를 통해 rev와 slow의 값이 모두 같을 경우 palindrome인 것을 알 수 있다. 그리고 palindrome일 경우에 위 루프를 돌아 rev에는 아무값도 남아있지 않게 될 것이다. 
        # 즉, rev는 None이며 이것을 bool타입으로 바꾸자면 False이다. 이것을 not을 통해 바꿔주면 palindrome이 맞다는 의미인 True를 반환할 수 있다.
        # palindrome 아닐 경우에는 rev에 데이터가 남아있게 되기에 True이다. 마찬가지로  이것을 not을 통해 바꿔주면 palindrome이 아니는 의미인 False를 반환할 수 있다.
        return not rev 