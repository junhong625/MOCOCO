class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(idx, s):
            if idx == len(digits):
                return
            for i in pn[digits[idx]]:
                s += i
                if idx == len(digits)-1:
                    result.append(s)
                dfs(idx+1, s)
                s = s[:-1]
            
        result = []
        pn = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        dfs(0, '')
        
        return result