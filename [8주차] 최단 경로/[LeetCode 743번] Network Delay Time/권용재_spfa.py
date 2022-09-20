'''
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
times = [[1,2,1]], n = 2, k = 1
times = [[1,2,1]], n = 2, k = 2

# u, v, w = 춮발지 / 도착지 / 소요시간
'''

def networkDelayTime(times, n, k):
    from collections import deque
    import sys
    inf = sys.maxsize
    

    # 인접 리스트 정보를 만들기 위한 adj_list 생성
    adj_list = [[] for _ in range(n+1)]
    # 거리 구하는 리스트
    distance = [0] + [inf] * n
    distance[k] = 0
    for u,v,w in times:
        adj_list[u].append((v,w))

    dq = deque()
    # 처음 걸린 시간(아직 출발을 안했기 때문에 0), 출발지점 append
    dq.append((0,k))
    while dq:
        time, node = dq.popleft()
        for v, w in adj_list[node]:
            # 도착지 까지의 소요 시간 최소로 갱신
            if time + w < distance[v]:
                distance[v] = time + w
                dq.append((time+w, v))

    # 도착하지 않는 정점이 있으면 -1 출력 그 이외에는 모든 노드를 1번씩 순회 해야하기 때문에 max를 뽑는다
    result = max(distance)

    if result == inf:
        return -1
    else: 
        return result

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

print(networkDelayTime(times, n, k))