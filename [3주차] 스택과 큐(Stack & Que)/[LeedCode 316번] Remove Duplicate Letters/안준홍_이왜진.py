from collections import deque
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = deque(sorted(set(s))) # 중복 제거 후 정렬, 속도를 조금이나마 높이기 위해 deque 사용
        duplicated_word = '' # s의 집합과 접두사 집합이 일치할 경우 접두사를 더해갈 변수
        
        # 접두사 집합에 해당하는 문자들을 우선적으로 걸러내기 위한 반복문
        while chars: 
            if set(s) == set(s[s.index(chars[0]):]): # 문자열 s와 chars에서 꺼낸 문자를 기준으로 잘라 만든 두 집합이 같을 경우 -> 해당 문자가 문자열 s의 제일 앞이라는 의미
                s = s[s.index(chars[0]):].replace(chars[0],'') # 위 조건에 충족할 경우 해당 s에서 해당 문자와 같은 문자들 모두 제거한 후 s에 저장
                duplicated_word += chars[0] # duplicated_word에 해당 문자 추가
                chars.popleft() # 1. 해당 문자는 duplicated_word에 추가 되었으니 제거
                chars = deque(sorted(set(s))) # 2. 이후 새로 생성된 s를 기준으로 집합과 정렬을 수행한 chars 생성
                continue # pop을 수행한 이후 다시 정렬한 집한 문자를 만들기 위해 위 1, 2번을 수행했으니 continue를 통해 바로 밑의 pop 피하기
            chars.popleft() # s의 집합과 접미사 집합이 일치하지 않을 경우 pop을 통해 가장 앞의 문자 제거
            
        new_word = "" # 좌측 방향으로 최솟값 비교 후 들어갈 문자열 
        new_word2 = "" # 우측 방향으로 최솟값 비교 후 들어갈 문자열
        
        # 좌측 방향으로 진행하며 new_word에 있는 문자가 또 나올 시 두 경우의 수를 비교하여 더욱 작은 값을 반환하는 반복문
        for i in range(len(s)-1, -1, -1): # 좌측 방향으로 진행
            if s[i] not in new_word:  
                new_word = s[i] + new_word 
            else:
                n = list(new_word)
                n.remove(s[i])
                n = "".join(n)
                n = s[i] + n
                new_word = min(new_word, n)
        
        # 우측 방향으로 진행하며 new_word에 있는 문자가 또 나올 시 두 경우의 수를 비교하여 더욱 작은 값을 반환하는 반복문
        for i in range(0, len(s)): # 우측 방향으로 진행
            if s[i] not in new_word2:
                new_word2 += s[i]
            else:
                n = list(new_word2)
                n.remove(s[i])
                n = "".join(n)
                n += s[i]
                new_word2 = min(new_word2, n)
        
        # 접미사 집합 반복문을 통해 걸러낸 문자열과 좌측 방향 필터와 우측 방향 필터 중 최솟값을 더해 반환        
        return duplicated_word + min(new_word, new_word2)