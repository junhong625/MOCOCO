from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):

        graph = defaultdict(list)
        for start, nxt in tickets:
            graph[start].append(nxt)

        for key in graph:
            graph[key].sort(reverse=True)

        result = []

        def dfs(node):
            while graph[node]:
                # reverse 를 해놨으니 해당 키에서 알파벳 순서대로 이동
                dfs(graph[node].pop())
            # 시작점 부터 기록
            result.append(node)

        dfs('JFK')
        return result[::-1]