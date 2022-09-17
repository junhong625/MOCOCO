class Solution(object):
    def networkDelayTime(self, times, n, k):
        
        nodes = collections.defaultdict(list)               # 각 노드에 갈 수 있는 방향과 가중치 할당
        for unit in times:
            nodes[unit[0]].append([unit[1], unit[2]])
        
        stack = [[k, 0]]
        visited = collections.defaultdict(list)             # 방문한 노드도 딕셔너리로 선언
        visited[k] = 0
        while stack:
            s = stack.pop(0)
            
            for unit in nodes[s[0]]:                        # 안 간 노드거나 현재 가중치값이 기존값보다 작을 때 (속도가 빠를 때)
                if unit[0] not in visited or unit[1] + s[1] < visited[unit[0]]:
                    visited[unit[0]] = unit[1] + s[1]       # 추가하거나 최신화
                    stack.append([unit[0], unit[1] + s[1]]) # 하고나서 스택에 어펜드
        
        res = 0
        for unit in visited:                                # 작업 완료 후 최대시간 탐색 (끝까지 도달한 시간)
            if res < visited[unit]:
                res = visited[unit]
        
        if len(visited) < n:                                # 방문 다 못했으면 -1, 다 했으면 도달시간
            return -1
        else:
            return res  # 1434ms(7.47%) / 15.4mb(95.83%)