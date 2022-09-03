import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 단순 생각나는 데크를 활용한 것
        # 리스트 안에 있는 것과 비교하는 방식
        sub = collections.deque()
        result = 0
        for i in s:
            if sub:
                if i in sub:
                    while sub:
                        p = sub.popleft()
                        if p == i:
                            break
            sub.append(i)
            if len(sub) > result:
                result = len(sub)

        return result

        # 슬라이딩 윈도우를 딕셔너리로 구현
        # 동일한 놈이 나오면 그 위치로 돌아가서 빼주기
        uesd = {}
        max_len = start = 0
        for index, i in enumerate(s):
            if char in used and start <= used[i]:  # 중복이라면
                start = used[i] + 1  # 시작지점 갱신
            else:
                max_len = max(max_len, index - start + 1)  # 아니면 시작지점이랑 현재 위치 거리 비교
            used[i] = index  # 딕셔너리에 지점 저장
        return  max_len
