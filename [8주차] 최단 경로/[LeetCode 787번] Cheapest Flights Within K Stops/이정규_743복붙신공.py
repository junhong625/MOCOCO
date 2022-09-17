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
        
        nodes = collections.defaultdict(list)               # 각 노드에 갈 수 있는 방향과 가중치 할당
        for unit in flights:
            nodes[unit[0]].append([unit[1], unit[2]])\

        stack = [[src, 0, k + 1]]
        visited = collections.defaultdict(list)             # 방문한 노드도 딕셔너리로 선언
        visited[src] = 0
        while stack:
            s = stack.pop(0)
                
            for unit in nodes[s[0]]:                        # 안 간 노드거나 현재 가중치값이 기존값보다 작을 때 (더 쌀 때)
                if unit[0] not in visited or unit[1] + s[1] < visited[unit[0]]:
                    if s[2] - 1 >= 0:                       # 경유지 횟수가 남아 있다면
                        visited[unit[0]] = unit[1] + s[1]                   # 추가하거나 최신화
                        stack.append([unit[0], unit[1] + s[1], s[2] - 1])   # 하고나서 스택에 어펜드
        
        if dst not in visited:                              # 도달 못했으면 -1, 했으면 최소비용
            return -1
        else:
            return visited[dst] #950ms(5.06%), 14.9mb(56.14%)