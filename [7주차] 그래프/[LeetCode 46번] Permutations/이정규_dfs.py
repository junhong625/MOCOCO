class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs (num_l, chk_l):
            #print(num_l, chk_l)
            if len(nums) == len(chk_l):
                res.append(chk_l)
                return
            
            for i, temp in enumerate(num_l):
                n = []
                n.extend(num_l[:i])
                n.extend(num_l[i + 1:])
                chk_l.append(temp)
                print(n, chk_l)
                dfs(n[:], chk_l[:])
                
        res = []
        chk = []
        dfs(nums, chk)
        return res #45ms / 13.8mb