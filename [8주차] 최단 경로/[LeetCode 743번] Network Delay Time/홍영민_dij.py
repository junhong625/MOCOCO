import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
            """
            :type times: List[List[int]]
            :type n: int
            :type k: int
            :rtype: int
            """

            graph = [[] for _ in range(n+1)]
            # 방문처리
            visited = [0] * (n + 1)
            # 거리 등록(100개 노드에 600 거리 곱 보다는 길게)
            distance = [6000000] * (n + 1)
            for i in times:
                graph[i[0]].append([i[1], i[2]])

            def small_node():
                min_value = 6000000
                index = 0
                for i in range(1, n+1):
                    if not visited[i] and distance[i] < min_value:
                        min_value = distance[i]
                        index = i
                return index

            def dijs(x):
                # 시작지점 거리값 0으로 지정 안함
                distance[x] = 0
            # n-1개의 노드 갯수 만큼 반복
                for _ in range(n-1):
                    print(distance)
                    now = small_node()
                    visited[now] = True
                    # 인접 노드들 간의 거리 계산
                    for next in graph[now]:
                        cost = distance[now] + next[1]
                        if cost < distance[next[0]]:
                            distance[next[0]] = cost
            dijs(k)
            # 반복문이 다 돌아가고도 다 방문하지 못한다면, -1을 return
            for i in distance[1:]:
                if i == 6000000:
                    return -1
            else:
                return max(distance[1:])

class Solution(object):
    def networkDelayTime(self, times, n, k):
            """
            :type times: List[List[int]]
            :type n: int
            :type k: int
            :rtype: int
            """
            graph = [[] for _ in range(n+1)]
            # 방문처리
            visited = [0] * (n + 1)
            # 거리 등록(최대값 100보다는 길게)
            distance = [101] * (n + 1)
            for i in times:
                graph[i[0]].append([i[1], i[2]])
            print(graph)

            q = []
            heapq.heappush(q,(0,k))
            distance[k] = 0
            while q:
                dist, node = heapq.heappop(q)
                if distance[node] < dist:
                    continue
                for next in graph[node]:
                    cost = distance[node] + next[1]
                    if cost < distance[next[0]]:
                        distance[next[0]] = cost
                        heapq.heappush(q, (cost,next[0]))
            return -1 if distance[n] == 101 and distance[n] == 0 else distance[n]