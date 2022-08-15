class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        window = deque() 
        
        for idx, num in enumerate(nums):
            while window and nums[window[-1]] < num: # 새로 들어온 값보다 작은 윈도우의 값들 모두 제거
                window.pop()
            window.append(idx) # 현재 idx 윈도우에 추가
            if window and window[0] == idx-k: # 윈도우의 첫번째 값 삭제 ex) 현재 idx값이 3이고 k가 3일 경우 윈도우에는 idx가 1,2,3만 들어갈 수 있다.idx-k이하의 수는 모두 삭제
                window.popleft()
            if idx >= k-1: # idx가 k-1에 도달했을 때부터 최대값 추가 ex) k=3일 때 0,1,2 즉 k-1부터 result에 최대값을 추가화면 된다.
                result.append(nums[window[0]]) # 위의 while문을 통해 작은 수들은 모두 pop을 했기에 윈도우의 첫번째 값이 최대값이 된다.
            
        return result