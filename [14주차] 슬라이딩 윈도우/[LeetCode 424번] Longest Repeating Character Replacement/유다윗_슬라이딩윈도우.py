# 424. Longest Repeating Character Replacement
# 4423ms / 14.1mb

# flow
# 1. 윈도우 크기를 s에서 줄여나가기
# 2. 윈도우를 첫 번째 letter부터 시작해서 오른쪽으로 옮겨가기
# 3. 윈도우 내 고유값 개수 - k 가 1 이하일 경우 해당 윈도우 길이가 정답


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_len = len(s)
        window = s_len - 1                                                              # window 초기화
        while window > 0:
            max_of_max = 1                                                              # max_count_letter의 최대값. window를 줄여나갈 때 사용하는 변수
            left = 0
            right = left + window
            while right < s_len:
                s_uniques_dict = defaultdict(int)

                for u in s[left:right+1]:                                               # 현재 window 구간의 각 letter별 개수 구하기
                    s_uniques_dict[u] += 1
                
                max_count_letter = max(s_uniques_dict.items(), key=lambda x: x[1])[1]   # 가장 많이 나온 letter의 개수
                if max_count_letter + k > max_of_max:                                   # max_count_letter 업데이트
                    max_of_max = max_count_letter + k
                key = (window+1) - max_count_letter - k                                 # 현재 구간에서 정답이 도출될 수 있는지 기준이 되는 값
                if key <= 0:
                    return window + 1                                                   # 정답 return
                else:
                    move = key // 2                                                     # 오른쪽으로 얼마나 움직일지 나타내는 변수
                    left += move if move > 0 else 1
                    right += move if move > 0 else 1
            window = max_of_max - 1                                                     # window 줄이기