class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chk = {}
        max_len = 0                                         # 최댓값
        start_at = 0                                        # 시작점
        for now, word in enumerate(s):
            if word not in chk or chk[word] < start_at:     # 없는놈이거나 시작점 이전 놈이면
                if max_len < now - start_at + 1:            # 최댓값 갱신
                    max_len = now - start_at + 1
            if word in chk and chk[word] >= start_at:       # 중복인데다 시작점 이후 놈이면
                start_at = chk[word] + 1                    # 시작점 갱신
                
            chk[word] = now                                 # 현재 문자 위치 입력
        
        if s and max_len < now - start_at + 1:              # 문자열 없을 때 혹은 공백일 때 예외처리
            max_len = now - start_at + 1
                
        return max_len
