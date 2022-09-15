class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        
        def dfs(idx):                   # dfs 재귀
            if visited[idx] == -1:      # 현재 진행 중인 dfs탐색에서 방문했던 idx에 또 방문했다는 것은 불가능한 코스라는 의미기에 False를 반환
                return False
            visited[idx] = -1           # 현재 진행 중인 dfs탐색에서 방문한 idx는 -1로 표시
            
            for w in adjList[idx]:      # 인접 리스트 순회 
                if visited[w] == 1:     # 이번 dfs탐색을 통해 방문을 했던 곳이라면 다음 순회로 이동
                    continue
                if not dfs(w):          # 인접 리스트의 값으로 dfs 탐색을 진행했으나 False가 나올 경우 False를 반환하고 종료
                    return False
            visited[idx] = 1            # 이번 dfs탐색에서 코스가 원활히 진행됐다면 방문했던 곳들 모두 1로 변경하고
            return True                 # True 반환
        
        adjList = defaultdict(list)     # defaultdict로 value의 기본형 list로 지정
        visited = [0 for _ in range(numCourses)] # 방문 기록
        for s, e in prerequisites:      # 인접 리스트에서 값 할당
            adjList[s].append(e)
        
        for i in range(numCourses):     # 0번 코스부터 순회 시작
            if not dfs(i):              # i번 코스에 대한 dfs 탐색이 False를 반환하면 False를 반환하고 종료
                return False
        return True                     # 코스를 모두 순회했음에도 False가 반환되지 않았다면 코스를 무사히 완료할 수 있다는 의미, True 반환