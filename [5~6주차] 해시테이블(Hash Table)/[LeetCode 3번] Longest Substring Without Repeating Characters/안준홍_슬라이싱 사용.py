class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Hash = [0] # 빈 데이터가 들어왔을 때 0을 반환하기 위해 먼저 0을 집어넣어둠
        chars = ''
        for char in s: # 문자열 순회
            if not chars or char not in chars:  # chars에 문자가 없거나 chars에 포함되지 않는 문자일 경우
                chars += char                   # chars에 추가         
            else:                                           # chars에 중복되는 문자가 있을 경우
                chars = chars[chars.index(char)+1:] + char  # 중복되는 부분까지 슬라이싱 한 후 중복되는 부분 추가
            Hash.append(len(chars))             # 위 작업들을 끝낸 후 현재 chars의 길이를 Hash에 추가
                
        return max(Hash)
            