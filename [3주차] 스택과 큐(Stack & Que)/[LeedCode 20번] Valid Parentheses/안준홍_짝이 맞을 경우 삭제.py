class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s에서 하나씩 pop을 하기 위해 문자열 타입에서 리스트 타입으로 변경
        s = list(s)
        stack = []
        # 짝이 맞는지 체크하기 위한 용도
        pairs = ['()','[]','{}']
        # s의 값이 모두 사라질 때 까지 반복
        while s:
            # s에서 마지막 값을 꺼내 stack리스트에 추가
            stack.append(s.pop())
            # stack리스트의 길이가 2이상일 경우에 비교가 가능함
            # 그리고 stack[-1]과 stack[-2]의 짝이 맞을 경우 삭제
            if len(stack) >= 2 and stack[-1] + stack[-2] in pairs:
                stack.pop()
                stack.pop()
                # stack = stack[:-2]
                # 호기심에 의해 슬라이싱과 두 번의 pop의 속도를 비교해본 결과 pop이 더 빠르게 결과를 가져온다.
        # stack이 남아 있는 경우(True) -> 짝이 맞지 않았다는 의미(False)
        # stack이 남아 있지 않은 경우(False) -> 짝이 맞았다는 의미(True)
        # 위와 같이 반환하기 위해 not을 통해 반대의 데이터를 반환
        return not stack
                    