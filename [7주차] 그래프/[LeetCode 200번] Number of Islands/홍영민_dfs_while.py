class Solution(object):

    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
#         스택으로 구현
#         m = len(grid)
#         n = len(grid[0])
#         delta = [(0,1),(1,0),(-1,0),(0,-1)]
#         result = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     start = (i,j)
#                     stack = [start]
#                     while stack:
#                         vi, vj = stack.pop()
#                         grid[vi][vj] = 0
#                         for di, dj in delta:
#                             if 0<=vi + di < m and 0 <= vj + dj < n and grid[vi+di][vj+dj] == "1":
#                                 stack.append((vi+di,vj+dj))
#                     result += 1
                                
#         return result

# 재귀로 구현
        def dfs(vi,vj,stack):
            stack.append([vi,vj])
            while stack:
                si, sj = stack.pop()
                grid[si][sj] = 0
                for di,dj in delta:
                    if 0<=si + di < m and 0 <= sj + dj < n and grid[si+di][sj+dj] == "1":
                        dfs(si+di,sj+dj,stack)
            return 1

        m = len(grid)
        n = len(grid[0])
        delta = [(0,1),(1,0),(-1,0),(0,-1)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    stack = []
                    result += dfs(i,j,stack)
        return result
