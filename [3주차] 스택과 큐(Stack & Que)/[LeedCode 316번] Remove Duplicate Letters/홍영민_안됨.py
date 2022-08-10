import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        구조화

        1. 중복되는가?
        2. 중복되면 남겨둘만한가?
        - '''
        # 뒤에서 부터 넣기는 abacb와 같이 앞에 a같은게 2번 들어가는 경우를 해석을 해주지 못한다
        #         from collections import deque
        #         s = list(s)
        #         differ = deque()
        #         for i in range(len(s)-1,-1,-1):
        #             k = s[i]
        #             if k not in differ:
        #                 differ.appendleft(k)
        #             else:
        #                 if k > differ[0]:
        #                     continue
        #                 else :
        #                     differ.remove(k)
        #                     differ.appendleft(k)
        #         result = ''.join(differ)
        #         return result
        # 앞에서부터 넣기, 또한 알파벳 순서와 이상한 예외가 많아서 되지 않았다
        # differ = list()
        # if len(s) <= 1:
        #     return s
        # for i in range(len(s)):
        #     k = s[i]
        #     if k not in differ:
        #         differ.append(k)
        #     else :
        #         # bab일경우 뒤에걸, aba일 경우 앞에걸 살려야 한다.
        #         for i in range(differ.index(k),len(differ)):
        #             if differ[i] < k:
        #                 differ.remove(k)
        #                 differ.append(k)
        # return ''.join(differ)

        # 책의 답지
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            print(stack)
            print(seen)
            seen.add(char)
        return ''.join(stack)