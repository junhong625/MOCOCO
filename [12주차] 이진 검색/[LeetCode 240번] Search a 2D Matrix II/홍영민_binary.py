class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 사각형의 전체 기준에서 분명하게 없을 정사각형의 크기를 잘라가면서 진행
        self.result = False
        def dfs(xl,yl,xr,yr):
            if self.result == True:
                return
            if xl <= xr and yl <= yr:
                newx = (xl+xr)//2
                newy = (yl+yr)//2
                out = matrix[newx][newy]
                print(out)
                if out == target:
                    self.result = True
                elif out > target:
                    dfs(xl,yl,newx-1,yr)
                    dfs(xl,yl,xr,newy-1)
                else:
                    dfs(newx+1,yl,xr,yr)
                    dfs(xl,newy+1,xr,yr)
            else:
                self.result = False
        dfs(0,0,len(matrix)-1,len(matrix[0])-1)
        return self.result