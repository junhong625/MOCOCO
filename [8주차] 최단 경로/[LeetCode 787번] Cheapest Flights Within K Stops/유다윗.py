from collections import defaultdict
from collections import defaultdict
import heapq

####### 테스트케이스 37번까지 통과 #######

def findCheapestPrice(n, flights, src, dst, k):
    # flights: [from, to, price]
    # obj.: src에서 dst까지 k개 경유지 이내로 가는 최소 비용 구하기

    graph = defaultdict(list)

    for u, v, w in flights:                                 # 인접리스트 만들기
        graph[u].append((v, w))                             # (to, price)
    
    if src not in graph.keys():
        return -1

    q = [(0, src, 0)]                                       # (시작점에서 정점까지 가격, 정점, 경유지 수-1)
    dist = defaultdict(int)                                 # 거리

    while q:                                                # q순회
        price, node, stop = heapq.heappop(q)                # 최소값 추출
        print(q, node)

        if stop == k+2:                                     # 허용된 경유지 수를 초과할 경우 continue
            continue
        elif (node == src and stop != 0):                   # 다시 시작점으로 회귀할 경우 break
            break

        dist[node] = price
        if node == dst:                                     # 목직지 도달 시 break
            break

        for v, w in graph[node]:
            alt = price + w
            heapq.heappush(q, (alt, v, stop+1))

    return dist[dst] if dist[dst]!= 0 else -1


if __name__ == '__main__':
    print(findCheapestPrice(4, [[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]], src = 3, dst = 0, k = 3))