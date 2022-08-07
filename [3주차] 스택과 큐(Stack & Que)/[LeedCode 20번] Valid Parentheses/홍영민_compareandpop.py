class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        valid = []
        # 1개도 안되면 당연히 false
        if len(s) <= 1:
            return False
        
        for idx,i in enumerate(s):
            if len(valid) == 0: # 첫번째 것은 입력을 해줘야 오류가 안난다
                valid.append(i)
                continue
            if i == ")":
                k = valid.pop()
                if k == '(':
                    result = True
                else :
                    valid.append(k)
                    valid.append(i)
            elif i == "]":
                k = valid.pop()
                if k == '[':
                    result = True
                else :
                    valid.append(k)
                    valid.append(i)
            elif i == "}":
                k = valid.pop()
                if k == '{':
                    result = True
                else :
                    valid.append(k)
                    valid.append(i)
            # 모든 조건에 대한 비교 / 추후 딕셔너리 활용시 시각적으로도 표현으로도 쉬워질 것이다
            else :
                valid.append(i)
                ## 만약 모든 조건이 만족한다면 결과값은 길이가 0이어야 한다.
        if len(valid) == 0:
            return True
        else : 
            return False