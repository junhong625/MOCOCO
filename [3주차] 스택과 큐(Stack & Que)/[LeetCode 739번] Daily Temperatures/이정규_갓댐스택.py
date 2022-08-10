class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        stack_idx= []
        cnt = []
        idx = 0
        
        for temp in temperatures :
                
            if stack and stack[-1] < temp :
                while stack and stack[-1] < temp : # stack에 숫자가 남아 있고, 다음에 올 숫자가 더 클 때
                    stack.pop()                    # stack에 있는 숫자 pop
                    take = stack_idx.pop()         # pop한 숫자에 해당하는 idx도 pop
                    cnt[take] = idx - take         # 다음에 올 숫자의 idx와 pop한 idx의 차를 cnt에 할당
                    
            stack.append(temp)          # 현재 숫자 stack에 저장
            stack_idx.append(idx)       # 현재 숫자의 인덱스 저장
            cnt.append(0)               # 현재 숫자 카운팅 추가
            idx += 1
        
        return cnt # 1701ms 20mb