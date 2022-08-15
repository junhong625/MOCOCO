class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''방법
        1. 주요 방식은 괄호의 인덱스들을 저장해서 그 사이의 간격 중 최대값을 계산하기로 하였다
        2. 괄호가 완성이 되면 stack에서 뺄것이다
        3. 위의 방법이라면 짝이 생기지 않은 여는 괄호들은 stack안에 남게 된다
        4. 만약 닫는 괄호가 먼저 나오거나 흐름을 끊는 역할을 한다면, 이는 여는 괄호와의 갯수 비교를 통해 stack안에 저장하기로 하였다
        5. 나머지는 예외처리를 해준다
        '''
        x, y = 0, 0                     # x,y는 여는 괄호의 갯수보다 닫는 괄호가 많아지는 경우를 방지하기 위한 것
        count, result = 0, 0
        index_stack = [0]       # 0을 준 이유는 이후 계산에서 시작점을 주기 위해서 이다
        # index를 stack으로 쌓아가며 중간에 이어지는 부분의 최대 값을 구하기로 하였다
        for idx,i in enumerate(s):
            if i == "(":                        # (가 들어오면 카운트 시작
                index_stack.append(idx+1)
                x += 1
            else :
                y += 1
                # print(x, y)
                if x < y or x == 0:            # 닫는 괄호 갯수가 많거나 0이라면 흐름을 끊는 것이다
                    x,y = 0,0
                    index_stack.append(idx+1)
                elif x >= y:
                    index_stack.pop()       # 아니라면 stack을 빼줌
                    y -= 1
                    x -= 1
                else:
                    index_stack.append(idx+1)   # 이도저도 아니라면 더하지만, 이는 아마 상관없는 구문일 것이다
        if index_stack == [0]:              # 만약 전체가 깔끔히 이어진다면 붙는게 없으므로 최대치인 len을 반환
            return len(s)
        index_stack.append(len(s) + 1)      # 이건, 계산이 이상해서 일단
        # print(index_stack)
        for i in range(len(index_stack)-1):
            count = index_stack[i+1]-index_stack[i] - 1     # 최대값 계싼
            result = max(result,count)
        if result == 1:         # 최대값이 1이란 소리는 하나도 이어진 것이 없는 것이므로 0을 반환
            return 0
        return result