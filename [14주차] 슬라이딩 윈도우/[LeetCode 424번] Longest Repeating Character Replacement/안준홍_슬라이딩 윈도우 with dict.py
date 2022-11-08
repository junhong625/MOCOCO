class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt_cur = dict()
        cur = ""
        answer = 0
        
        for char in s:
            cnt_cur[char] = cnt_cur.get(char,0) + 1
            cur += char
            while True:
                if len(cnt_cur) > k+1 or len(cur) - max(cnt_cur.values()) > k:
                    cnt_cur[cur[0]] -= 1
                    if not cnt_cur[cur[0]]:
                        del cnt_cur[cur[0]]
                    cur = cur[1:]
                    continue
                break
            answer = max(answer, len(cur))
        return answer