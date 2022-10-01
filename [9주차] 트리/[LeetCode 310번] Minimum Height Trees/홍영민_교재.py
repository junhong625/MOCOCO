class Solution(object):
    def findMinHeightTrees1(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # 그래프 생성 후 전체 탐색 진행
        # 이 경우 모든 경우의 수를 탐색하기 때문에 시간초과가 발생
        def tree(x, h):
            if x < n:
                visited[x] = True
                for i in graph[x]:
                    if visited[i] == False:
                        tree(i, h + 1)
                else:
                    if self.height < h:
                        self.height = h
                        return
            else:
                return

        min_height = 2 * 10 ** 4
        graph = [[] for _ in range(n)]
        result = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        for i in range(n):
            self.height = 0
            visited = [0] * n
            tree(i, 1)
            if self.height < min_height:
                min_height = self.height
                result = [i]
            elif self.height == min_height:
                result.append(i)
        return result
        # 따라서 반대로 단계가 중간에 껴있는 친구들을 루트로 가져가야 한다()

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 그래프 생성 후 전체 탐색 진행
        # 이 경우 모든 경우의 수를 탐색하기 때문에 시간초과가 발생
        if n <= 1:
            return [0]
        graph = [[] for _ in range(n)]
        leaves = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                near = graph[leaf].pop()  # leaf이기에 더이상 필요 없으니 공백으로 만들어 버림
                graph[near].remove(leaf)  # 인접 노드에 삭제될 리프 삭제

                if len(graph[near]) == 1:  # 삭제 후, 남은 인접노드가 1이면 그건 이제 새 리프
                    new_leaves.append(near)
            leaves = new_leaves
        return leaves  # 마지막 선택된 놈들이 최후임