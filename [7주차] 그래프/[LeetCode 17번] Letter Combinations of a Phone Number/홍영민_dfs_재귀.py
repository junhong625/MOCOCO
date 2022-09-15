class Solution(object):
    
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 입력과 같은 위치에 알파벳 할당
        # 귀찮지만 그냥 해야지...
        output = [[],[],["a",'b',"c"],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        result = []
        # 재귀로 할당, result에 바로 저장
        def dfs(x,word):
            if x == len(digits):
                result.append(word)
                return
            else:
                for k in output[int(digits[x])]:
                    # print(word + k)
                    dfs(x+1, word + k)
        # 빈 글자열에 대해서 ['']를 반환하므로 예외 처리
        if not digits:
            result = []
        else:
            dfs(0,'')
        return result 