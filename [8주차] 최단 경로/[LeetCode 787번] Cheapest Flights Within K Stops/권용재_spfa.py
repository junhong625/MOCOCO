'''
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

# n : 노드수 / flights: [from, to, price] / src : 출발지 / dst: 도착지 / k : 경유지 개수
'''


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    from collections import defaultdict
    import sys
    inf = sys.maxsize

    # 그래프 정보 만들기
    graph = defaultdict(dict)
    for start, nxt, price in flights:
        graph[start][nxt] = price

    print(graph)
    
    prices = [inf] * n
    prices[src] = 0

    q = [src]

    while q and k >=0:
        next_q = []
        next_prices = [p for p in prices]
        for city in q:
            for nxt in graph[city]:
                if prices[city] + graph[city][nxt] < next_prices[nxt]:
                    next_prices[nxt] = prices[city] + graph[city][nxt]
                    next_q.append(nxt)
        q = next_q
        prices = next_prices
        k -=1
    print(prices)
    return -1 if prices[dst] == inf else prices[dst]

print(findCheapestPrice(n, flights, src, dst, k))