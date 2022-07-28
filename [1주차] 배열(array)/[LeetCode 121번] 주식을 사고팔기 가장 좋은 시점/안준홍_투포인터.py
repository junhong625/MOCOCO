class Solution:
    def maxProfit(self,prices):
        # small값 포인터
        left = 0 
        # big값 포인터
        right = 1
        # 최대값
        max_price = 0
        # big값 포인터가 끝까지 이동하면 종료
        while right < len(prices):
            # 현재 가격
            price = prices[right] - prices[left]
            # 현재 가격이 - 일 경우 left포인터를 right포인터로 이동
            if price < 0:
                left = right
            # 가격이 + 이며 max_price보다 클 경우 max_price를 price값으로 변경
            else:
                if max_price < price:
                    max_price = price
            # 위 식을 모두 수행 후 big 값 포인터 오른쪽으로 한칸 이동
            right += 1
        return max_price