from collections import defaultdict


class Solution(object):
    def canFinish1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        go = [[0] * numCourses for _ in range(numCourses)]
        requisite = [[0] * numCourses for _ in range(numCourses)]
        que = deque()
        for j in prerequisites:
            go[j[0]][j[1]] += 1
            requisite[j[1]][j[0]] += 1
        for i in range(numCourses):
            if sum(go[i]) == 1:
                que.append(i)
        if not que:
            return False
        print(requisite)
        while que:
            start = que.popleft()
            for i in requisite:
                i[start] = 0
            for idx, i in enumerate(requisite[start]):
                if i == 1 and sum(requisite[idx]) == 0:
                    requisite[start][idx] = 0
                    que.append(idx)
        return True if not que else False

    ## 교재 코드
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()
        visited = set()

        def dfs(i):
            # 판독하는 부분
            if i in traced:  # 순환구조이면, 탈출(못하는 거라서)
                return False
            if i in visited:  # 방문한 곳이면 일단은 그냥 고
                return True

            traced.add(i)
            for y in graph[i]:  # 연결된 부분 전체 파악
                if not dfs(y):  # 순환 여부 확인
                    return False

            traced.remove(i)  # 이제 이친구는 순환 확인에 필요없음
            visited.add(i)  # 방문 처리
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True
