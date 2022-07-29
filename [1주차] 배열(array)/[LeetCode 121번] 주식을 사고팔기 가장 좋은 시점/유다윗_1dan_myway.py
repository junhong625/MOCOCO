class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 리스트 원소가 1개일 경우 거래가 불가능하므로 바로 종료
        if len(prices) == 1:
            return 0

        min_now = 0
        max_now_idx = 0
        result = 0

        while True:
            # 리스트의 최대값을 찾는다.
            max_new = max(prices[max_now_idx+1:])

            # 새로운 최대값이 0이면 종료
            if max_new == 0:
                break
            
            # 새로운 최대값의 인덱스와, 새로운 최소값을 구한다.
            max_new_idx = prices[max_now_idx+1:].index(max_new) + len(prices[:max_now_idx+1])
            min_now = min(prices[max_now_idx:max_new_idx])

            # 최대값-최소값이 커지면 result 업데이트
            if result < max_new - min_now:
                result = max_new - min_now

            max_now_idx = max_new_idx
            
            # 최대값 인덱스가 리스트 끝에 다다르면 종료
            if (max_now_idx == (len(prices)-1)):
                break

        return result if result > 0 else 0