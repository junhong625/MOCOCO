# 76. Minimum Window Substring


# 265 / 267
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):                                         # t가 더 길면 조건을 충족할 수 없으므로 '' 반환
            return ''

        t_dict = defaultdict(int)                                   # key: letter, value: letter별 개수
        for letter in t:
            t_dict[letter] += 1
        
        window = len(t)
        while window <= len(s):
            left = 0
            right = left + window - 1
            window_add = window
            while right < len(s):
                now_s = s[left:right+1]
                now_s_dict = defaultdict(int)
                
                for letter in now_s:
                    now_s_dict[letter] += 1

                deficit = 0
                for (letter, count) in t_dict.items():
                    if count > now_s_dict[letter]:                  
                        deficit += (count - now_s_dict[letter])     # 부족한 letter의 개수 추가
                if not deficit:                                     # 부족분이 없으면 현재 now_s가 정답
                    return now_s
                else:
                    left += deficit                                 # 부족분만큼 이동
                    right += deficit
                    if deficit < window_add:
                        window_add = deficit
            window += window_add                                    # window 폭 증가시키기
        return ''