class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        k = collections.defaultdict(list)
        for i in tickets:
            k[i[0]] += [i[1]]
        # 사전순으로 정렬
        for j in k:
            k[j] = sorted(k[j])

        stack = []

        def dfs(x):
            while k[x]:  # 첫번째 값 읽어서 진행
                dfs(k[x].pop(0))
            stack.append(x)  # 먼저 가서 뒤에 붙여버림

        dfs('JFK')

        return stack[::-1]
