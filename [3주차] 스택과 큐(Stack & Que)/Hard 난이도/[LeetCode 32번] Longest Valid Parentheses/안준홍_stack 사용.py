class Solution(object):
    def longestValidParentheses(self, s):
        from collections import Counter, deque
        """
        :type s: str
        :rtype: int
        """
        stack = [] # 괄호들이 들어갈 stack구조의 리스트
        cnt_list = [] # 몇 개의 괄호들이 삭제 됐는지 기록되는 리스트 
        cur_idx = [] # stack에 남아있는 괄호들의 idx
        idx_list = [] # 괄호가 삭제될 때마다의 cur_idx가 기록될 리스트
        
        s = deque(s.lstrip(')').rstrip('(')) # 좌우 필요없는 괄호 삭제, que 타입으로 변환
        
        # 각 상황을 기록하는 구역
        idx, cnt = 0, 0 # 현재 idx와 cnt
        while s: # s에서 문자가 모두 삭제될 때까지 진행
            stack.append(s.popleft()) # s의 가장 앞 문자열을 stack에 추가
            cur_idx.append(str(idx)) # 해당 문자열의 idx를 cur_idx에 기록
            idx += 1 # idx += 1
            if len(stack) >= 2 and stack[-2] + stack[-1] == '()': # 짝이 맞은 괄호가 stack에 쌓일 경우 삭제
                for _ in range(2): # 카운트 + 2, stack에서 해당 괄호를 삭제, cur_idx에서 idx를 삭제
                    cnt += 1
                    stack.pop()
                    cur_idx.pop()
                if s and stack and stack[-1] + s[0] == '()': # 바로 괄호가 짝이 맞을 경우 
                    continue
                elif len(s) > 1 and s[0] + s[1] == '()': # 바로 괄호가 짝이 맞을 경우
                    continue
                else: # 다음에 바로 삭제가 어려운 경우 idx_list와 cnt_list에 현 상황을 기록
                    while idx_list and "".join(cur_idx) < idx_list[-1]: # 현재의 남은 idx가 idx_list의 마지막 기록보다 작을 경우 해당 기록을 삭제하고 현재의 idx를 추가
                        idx_list.pop()
                        cnt_list.pop()
                    cnt_list.append(cnt)
                    idx_list.append("".join(cur_idx))


        # 경우의 수를 계산하여 결과를 반환하는 구역

        if not cnt_list: # cnt_list에 아무것도 기록이 안 되어 있을 경우
            return 0
    
        elif len(cnt_list) == 1: # cnt_list가 딱 하나만 들어있을 경우
            return cnt_list[0] 

        result = [] # 경우의 수들을 기록한 리스트
        if '' in idx_list: # stack이 비어있는 상태로 기록된 idx가 있을 경우 가장 큰 값을 result에 기록
            for i in range(len(idx_list)-1,-1,-1):
                if idx_list[i] == '':
                    result.append(cnt_list[i])
                    break
        
        result.append(cnt_list[0]) # 각 기록들의 cnt차이를 저장
        for i in range(1, len(cnt_list)):
            result.append(cnt_list[i] - cnt_list[i-1])
            
        A = Counter(idx_list) 
    
        if A[max(A, key= lambda x:A[x])] >= 2: # 기록된 idx중 중복이 존재하는 경우
            for j in A:
                if A[j] >= 2: # 중복 되는 것들만
                    duplicate = [] 
                    for i in range(len(cnt_list)): 
                        if idx_list[i] == j: # 중복인 idx의 경우
                            if not duplicate and i != 0: # duplicate가 비어있고 idx가 0이 아닌 경우 이전 cnt값을 저장
                                duplicate.append(cnt_list[i-1])
                            elif i == 0: # index가 0인 경우 0을 저장
                                duplicate.append(0)
                            else: # 위 두 조건에 해당하지 않는 경우 해당 idx를 가지는 cnt를 저장 
                                duplicate.append(cnt_list[i]) 
                    result.append(max(duplicate)-min(duplicate)) # duplicate의 최대값과 최소값의 차이를 저장 
            
        return max(result) # 최대값을 반환