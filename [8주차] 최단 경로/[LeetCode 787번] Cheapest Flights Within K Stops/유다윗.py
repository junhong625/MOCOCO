from collections import defaultdict
from collections import defaultdict
import heapq

####### 테스트케이스 47/51번까지 통과 #######

def findCheapestPrice(n, flights, src, dst, k):
    # flights: [from, to, price]
    # obj.: src에서 dst까지 k개 경유지 이내로 가는 최소 비용 구하기

    graph = defaultdict(list)

    for u, v, w in flights:                                 # 인접리스트 만들기
        graph[u].append((v, w))                             # (to, price)
    
    if src not in graph.keys():                             # src에서 출발하는 경우가 없으면 바로 -1 return
        return -1

    q = [(0, src, 0)]                                       # (시작점에서 정점까지 가격, 정점, 경유지 수-1)
    dist = defaultdict(int)                                 # 거리

    while q:                                                # q순회
        price, node, stop = heapq.heappop(q)                # 최소값 추출

        if stop == k+2:                                     # 허용된 경유지 수를 초과할 경우 continue
            continue
            
        dist[node] = price
        if node == dst:                                     # 목적지 도달 시 break
            break

        for v, w in graph[node]:
            alt = price + w
            heapq.heappush(q, (alt, v, stop+1))

    return dist[dst] if dist[dst]!= 0 else -1


if __name__ == '__main__':
    print(findCheapestPrice(7, [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]],
     src = 2, dst = 4, k = 1))