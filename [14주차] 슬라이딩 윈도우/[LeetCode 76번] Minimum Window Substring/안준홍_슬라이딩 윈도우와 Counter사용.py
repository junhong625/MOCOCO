class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        target, n = Counter(t), len(t)                          # target : t의 문자 개수들, n : t의 길이
        answer = ""                                             # 정답
        cur = ""                                                # 현재 문자열
        
        for char in s:                                          # s를 char로 하나씩 꺼내서 순회
            if char in target:                                  # char가 target안에 존재할 경우
                if target[char] > 0:                            # target에 char 개수가 양수일 경우에만
                    n -= 1                                      # t에서 문자가 빠진걸로 판단하여 -1
                target[char] -= 1                               # target에서 char 개수 -1
            cur += char                                         # cur에 char 더해주기
            if not n:                                           # target에 필요한 모든 문자들이 cur에 들어있을 경우
                while cur:                                      # target에 들어있는 문자가 빠지면서 해당 문자를 s에서 가져와야할 경우까지 반복하거나 cur이 존재하는 동안 반복
                    if not answer or len(answer) > len(cur):    # answer가 존재하지 않거나 cur이 answer보다 짧을 경우에만 
                        answer = cur                            # 정답 변경
                    if cur[0] in target:                        # cur의 첫번째 문자가 target에 존재하는 문자일 경우
                        target[cur[0]] += 1                     # target에서의 char 개수 +1
                        if target[cur[0]] > 0:                  # 그 후에 char의 개수가 양수가 된다면 해당 문자가 필요해진 것으로 판단
                            cur = cur[1:]                       # 제일 앞 문자 제거
                            n += 1                              # 필요한 문자 개수 + 1
                            break                               # while문 종료
                    cur = cur[1:]                               # if문에 걸려 종료 되지 않았다면 제일 앞 문자 제거
                            
                
        return answer                                           # s를 모두 순회 후 정답 반환
            