class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        que = collections.deque()
        i = j = 0
        ans = []
        while j < len(nums):
            while len(que) > 0 and que[-1] < nums[j]:
                
                que.pop()
                
            que.append(nums[j])
            
            if j < k-1:
                
                j += 1
                
            elif j - i + 1 == k:
                
                ans.append(que[0])
                
                if nums[i] == que[0]:
                    
                    que.popleft()
                    
                i += 1
                j += 1
                
        return ans
