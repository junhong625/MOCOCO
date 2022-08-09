class Solution:
    def isValid(self, s: str) -> bool:

        # # s의 개수가 홀수일 경우 짝이 안 맞기 때문에 바로 False return
        # if len(s) % 2 == 1:
        #     return False

        # table= {
        #     '(': ')',
        #     '[': ']',
        #     '{': '}'
        # }

        # # case 1: ([]) <- 이런 형태인 경우
        # stack = []
        # for i in range(len(s)//2):
        #     stack.append(s[i])
        # if len(stack) % 2 != 1:
        #     for i in range(len(s)//2, len(s)):
        #         if table.get(stack.pop()) == s[i]:
        #             continue
        #         else:
        #             break
        #     else:
        #         return True
        
        # # case 2: ()[] <- 이런 형태인 경우
        # stack_1 = []
        # stack_2 = []
        # for i in range(0, len(s), 2):
        #         stack_1.append(s[i])
        #         stack_2.append(s[i+1])
        # if len(stack_1) == len(stack_2):
        #     for i in range(len(s)//2):
        #         if table.get(stack_1.pop()) == stack_2.pop():
        #             continue
        #         else:
        #             return False
        #     else:
        #         return True
        # else:
        #     return False
        

       #######################################
       # 위 방법은 실패. case 1과 2만 통과할 수 있는 줄 알았는데
       # (([]){}) <- 이런 것도 됨
       # 대칭적인 형태만 가능하다고 착각함
       #######################################

        ## 교재에 있는 방식 말고 다른 방법이 마땅히 떠오르지 않음 ##

        # s의 길이가 홀수면 짝이 없기 때문에 바로 False
        if (len(s) % 2 == 1):
            return False

        stack = []
        table= {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:
            # 문자가 key에 속하면 stack에 append
            if i in table.keys():
                stack.append(i)
            # stack에 원소가 없거나 괄호의 짝이 맞지 않을 경우 False
            elif not stack or table.get(stack.pop()) != i:
                return False
        else:
            # 짝이 다 맞아 stack의 모든 원소가 제거되었을 경우 True
            if len(stack) == 0:
                return True
            else:
                return False
                
