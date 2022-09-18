class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict, deque
        
        min_prices = [float('inf') for _ in range(n)]   # 각 경유지의 저렴한 항공권 가격이 들어갈 리스트
        adjNode = defaultdict(list)                     # 인접 경유지 
        while flights:                                  # 항공권이 존재할 경우 반복
            s, e, price = flights.pop()                 # 출발지, 도착지, 항공권 가격
            adjNode[s].append([e, price])               # 각 경유지에 항공권의 루트 표시
        
        q = deque([[src ,0, k+1]])                      # src : 나의 출발지, 0 : 항공권 가격, k+1 경유 횟수(k를 0이 될 때 까지 반복하기 위해)
        while q:                                        # q가 존재할 경우 반복
            idx, total_price, k = q.popleft()           # q의 첫번째 데이터를 추출 
            if k == -1:                                 # k가 0이 될 경우까지만 작업하기 위해 -1이 되면 종료
                break
            if min_prices[idx] > total_price:           # 현재 경유지의 최소값이 새로 들어온 값과 비교하여 더 클 경우
                min_prices[idx] = total_price           # 새로 들어온 값으로 현재 경유지의 값 변경
                for w, t in adjNode[idx]:               # 현재 목적지에서 이동 가능한 다음 경유지들을 순회, w : 이동 가능한 목적지, t : 해당 경유지로 이동하는 항공권의 가격
                    q.append([w, t+total_price, k-1])   # 다음 목적지, 현재 가격과 항공권 가격을 더합 값, 남은 이동 횟수를 q에 추가
        
        return min_prices[dst] if min_prices[dst] != float('inf') else -1 # 목적지의 가격이 무한일 경우 -1을 반환 아닐 경우 목적지의 가격 반환
                    