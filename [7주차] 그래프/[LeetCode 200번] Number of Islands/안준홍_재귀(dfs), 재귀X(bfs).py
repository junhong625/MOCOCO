class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        # recursion
        def dfs(x, y): # 재귀 풀이
            grid[x][y] = 0 
            for dx, dy in [[0,1], [1,0], [0, -1], [-1, 0]]: # delta 순회
                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == '1':
                    dfs(x+dx, y+dy)         
            
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt
        # 재귀 아닌 풀이
#         cnt = 0
#         q = deque()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     q.append([i, j])
#                     grid[i][j] = 0
#                     while q:
#                         x, y = q.popleft()
#                         for dx, dy in [[0,1], [1,0], [0, -1], [-1, 0]]:
#                             if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == '1':
#                                 grid[x+dx][y+dy] = 0
#                                 q.append([x+dx, y+dy])
                                
#                     cnt += 1
#         return cnt