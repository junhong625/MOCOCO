class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import collections
        
        adjNode = collections.defaultdict(list)             # 인접 노드 생성
        
        for u, v, w in times:                               # 인접 노드에 이동 가능한 노드 번호와 이동하는데 소요되는 시간 삽입
            adjNode[u].append([v,w])
        
        min_dis = [0] + [float('inf') for _ in range(n)]    # 각 노드까지의 최단 이동 시간, index를 맞춰주기 위해 맨 앞에 0으로 padding
        q = collections.deque([[k,0]])                      # q 생성

        while q:                                            # q가 존재할 경우 반복
            idx, time = q.popleft()                         # q에서 첫번째 값 추출
            if min_dis[idx] > time:                         # 기존의 최단 이동 시간 보다 새로 입력된 최단 이동 시간이 작을 경우 
                min_dis[idx] = time                         # 두 값을 교환
                for e, t in adjNode[idx]:                   # 현재 노드의 최단 이동 시간이 업데이트 되었기에 현재 노드에서 이동 가능한 노드들에 이것을 반영하기 위해 순회하며 반영된 시간을 q에 추가
                    q.append([e, t+time])
        
        m = max(min_dis)                                    # min_dis에서 가장 큰 값이 최종적으로 이동할 수 있는 곳까지 최단 이동 시간으로 이동 한 값
        
        return m if m != float('inf') else -1               # m이 float('inf')와 다르다는 것은 모두 방문을 했다는 의미이기에 m값을 그대로 반환하고, m이 float('inf')와 같다는 것은 이동하지 못한 곳이 있다는 의미이기에 -1을 리턴