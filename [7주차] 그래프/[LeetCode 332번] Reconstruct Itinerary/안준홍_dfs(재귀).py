class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(route): # 재귀 dfs
            if result: # 정답이 나왔을 경우 정지
                return
            elif len(route) == len(tickets)+1: # 가능한 루트가 나왔을 경우 해당 루트 result에 추가
                result.append(route)
                return
            elif route[-1] not in adjList: # 마지막 루트의 다음 장소가 없을 경우 정지
                return
            for _ in range(len(adjList[route[-1]])): # 방문 가능 지역의 수만큼 순회
                w = adjList[route[-1]].pop(0) # 방문할 지역 설정
                dfs(route+[w]) # 방문할 지역을 route에 추가해서 다음 탐색 실시
                if result: # 탐색 후 정답이 나왔을 경우 순회 종료
                    return
                adjList[route[-1]].append(w) # 다음 탐색 후 정답이 나오지 않았다면 방문 가능 지역 복구
                
        adjList = {}
        for s, a in sorted(tickets): # 방문 가능 지역 목록 설정
            if s in adjList:
                adjList[s].append(a)
            else:
                adjList[s] = [a]
        result = []
        dfs(['JFK'])
            
        return result[0]