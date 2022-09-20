from collections import defaultdict
import heapq

def networkDelayTime(times, n, k):
    graph = defaultdict(list)

    for u, v, w in times:                           # 인접리스트
        graph[u].append((v, w))

    q = [(0, k)]                                    # (시작점에서 정점까지 소요시간, 정점)
    dist = defaultdict(int)                         # 거리

    while q:                                        # q순회
        time, node = heapq.heappop(q)               # 최소값 추출
        if node not in dist:                        # 초기값이 없기 때문에 이 작업을 수행
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    return -1


if __name__ == '__main__':
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))# 출발지, 도착지, 소요시간