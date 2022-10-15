# 973. K Closest Points to Origin
# 1161ms / 20.2mb

# flow
# 1. x, y좌표 각각의 제곱 합 구하기
# 2. 정렬하기
# 3. k번째까지의 원소 뽑기

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        f_square = lambda x : [x[0]**2 + x[1]**2, x]            # x,y 좌표 제곱합을 첫 번째 원소로, 좌표를 두 번째 원소로 하는 리스트 만드는 함수
        points_sorted = sorted(list(map(f_square, points)))     # 정렬
        
        f_result = lambda x : x[1]                              # 좌표만 추출하는 함수
        result = list(map(f_result, points_sorted[:k]))         # k-1 인덱스까지의 좌표만 result에 담기
            
        return result