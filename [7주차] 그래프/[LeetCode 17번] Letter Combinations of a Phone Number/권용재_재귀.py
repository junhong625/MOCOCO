class Solution:
    def letterCombinations(self, digits):
        def add_substring(s, n):
            if n == L:
                ans.append(s)
                return
            for i in dict[digits[n]]:
                add_substring(s+i, n+1)
        if digits == '':
            return []

        L = len(digits)

        ans = []
        dict={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}

        add_substring("", 0)
        return ans