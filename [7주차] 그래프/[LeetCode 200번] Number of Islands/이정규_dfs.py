class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        stack = []
        union = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    if visited[y][x] == 0:
                        union += 1
                        stack.append((y, x))
                        while stack:
                            s = stack.pop()
                            visited[s[0]][s[1]] = 1
                            for i in range(4):
                                if 0 <= s[0] + d[i][0] < m and 0 <= s[1] + d[i][1] < n:
                                    if grid[s[0] + d[i][0]][s[1] + d[i][1]] == "1":
                                        if visited[s[0] + d[i][0]][s[1] + d[i][1]] == 0:
                                            stack.append((s[0] + d[i][0], s[1] + d[i][1]))
        return union
                                    
                            