class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        col = len(grid)
        row = len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < col and 0<= j < row and grid[i][j] == '1':
                grid[i][j] = '0'
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    dfs(i + dx, j + dy)

        island = 0
        for i in range(col):
            for j in range(row):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)
                    
        return island