class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def typing (s, strs):
            if len(digits) == len(strs):
                res.append(strs)
                return
            
            for chr in bunho[digits[s]]:
                typing(s + 1, strs + chr)
        
        
        bunho = { '2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
        
        if digits:
            res = []
            s = 0
            typing(s, '')
            return res
        
        else:
            return []   # 30ms / 13.8mb