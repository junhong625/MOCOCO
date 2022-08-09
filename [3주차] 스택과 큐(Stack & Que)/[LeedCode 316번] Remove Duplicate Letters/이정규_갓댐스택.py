class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []          # 스택쓰라니까 억지로 쓰는 스택배열
        alpha = [0] * 26    # ord('str') - ord('a') 해서 카운팅할 배열
        fixed = []       # 이미 자리고정된(혹은 될 예정인) 애들 모음
        
        for str in s :
            alpha[ord(str) - ord('a')] += 1 # 각 문자가 몇 개나 들어있는지 카운팅
        
        for str in s :
            
            if str in fixed :   # 중복되서 나타나면
                alpha[ord(str)- ord('a')] -= 1 # 카운팅 갯수 감소시키고 끝
                continue
            
            # 쌓여있는 문자열이 존재하면서, 마지막 문자가 다음에 올 문자보다 뒷문자이며
            # 앞으로 더 나타날 갯수가 있다면
            while stack and (ord(stack[-1]) > ord(str)) and (alpha[ord(stack[-1]) - ord('a')] > 0) :
                    fixed.remove(stack[-1]) # 고정값에서 없애고
                    stack.pop()             # 문자열에서도 빼고
            
            alpha[ord(str)- ord('a')] -= 1  # 카운팅에서 감소
            stack.append(str)               # 다음에 올 문자 붙이기
            fixed.append(str)               # 다음에 올 문자 고정
            
        return (''.join(stack))             # 아 쁘린뜨~  26ms 13.7mb
