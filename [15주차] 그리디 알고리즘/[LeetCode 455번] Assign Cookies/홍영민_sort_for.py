class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 가장 큰 친구에게 가장 큰 쿠키를 준다
        # 안맞으면 패스, 작은 친구로 넘어감
        # 맞으면 주고 카운트
        # 만약 다 없어지면 오류 날 수 있으니 break 걸어줌
        g.sort(reverse=True)
        s.sort()
        result = 0
        for i in g:
            if not s:
                break
            if i <= s[-1]:
                s.pop()
                result += 1
        return result