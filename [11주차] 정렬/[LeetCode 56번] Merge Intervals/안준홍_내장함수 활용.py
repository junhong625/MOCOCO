class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                                        # 크기 순 정렬
        stack = []                                              # 스택에 각 interval 추가
        while intervals:                                        # intervals가 있을 경우 반복
            stack.append(intervals.pop(0))                      # intervals의 첫번째 원소 추출해서 stack에 추가
            if len(stack) > 1 and stack[-2][-1] >= stack[-1][0]:# stack에 범위 리스트가 두 개 이상 존재할 경우 뒤쪽에 존재하는 범위 리스트의 첫번째 원소가 앞쪽에 존재하는 범위 리스트의 마지막 원소 이상일 경우
                s1 = stack.pop()                                # 뒤쪽의 원소 추출
                s2 = stack.pop()                                # 앞쪽의 원소 추출
                stack.append([s2[0], max(s1[-1], s2[-1])])      # stack에 합친 값을 추가
        return stack