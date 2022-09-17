class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        digits_letter={ '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}

        if digits == '':
            return []

        result = digits_letter[digits[0]]

        if len(digits) == 1:
            return result

        for i in digits[1:]:
            temp = []
            for j in digits_letter[i]:
                add = [i+j for i in result]
                temp.extend(add)
            result = temp
        return result