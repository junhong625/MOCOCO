# 76. Minimum Window Substring

# 575ms / 14.8mb
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):                                         # t가 더 길면 조건을 충족할 수 없으므로 '' 반환
            return ''

        target = Counter(t)
        target_keys = target.keys()
        result = '0' * (len(s) + 1)

        left = 0
        right = 0
        while right < len(s):
            left_flag = False
            while right < len(s):
                if s[right] in target_keys:
                    target[s[right]] -= 1
                    if len(list(filter(lambda x: x <= 0, list(target.values())))) == len(target):
                        right += 1
                        left_flag = True
                        break
                right += 1
            while left_flag and left < len(s):
                if s[left] in target_keys:
                    target[s[left]] += 1
                    if target[s[left]] > 0:
                        if len(result) > len(s[left:right]):
                            result = s[left:right]
                        left += 1
                        break
                left += 1
        return result if len(result) != (len(s) + 1) else ''



########################################################################################

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