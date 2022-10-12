# 56. Merge Intervals
# 367ms / 18.1mb

# flow
# 1. stack 만들기 -> intervals에서 stack으로 아래 과정에 따라 옮기기
# 2. stack에 아이템이 있을 경우, top의 end와 새로 들어오는 리스트의 start 비교
# 3. 구간이 겹치면 merge, 아니면 그냥 push

import heapq
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)                        # heap으로 변환
        stack = deque()                                 # stack

        while intervals:
            itv = heapq.heappop(intervals)              # intervals에서 start가 가장 작은 원소 추출
            if stack:                                   # stack에 원소가 있을 경우
                item = stack.pop()
                if item[1] >= itv[0]:                   # item의 end가 itv의 start보다 크거나 같을 경우 merge
                    if item[1] >= itv[1]:               # itv가 item에 포함될 경우
                        stack.append(item)
                    else:
                        stack.append([item[0], itv[1]])
                    continue
                stack.append(item)                      # merge가 발생하지 않으면 stack에 다시 집어넣기
            stack.append(itv)                           # stack에 원소가 없거나, merge가 발생하지 않으면 stack에 itv 넣기
        
        return stack