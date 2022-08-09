class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        comp = {')' :'(', ']' : '[', '}' : '{'}
        
        for unit in s :    
        
            stack.append(unit)
            
            if unit in comp :
                
                if len(stack) != 1 and stack[-2] == (comp.get(stack[-1])) :
                    stack.pop()
                    stack.pop()
                    
                else :
                    return False
        
        return len(stack) == 0 # 31ms, 13.4mb