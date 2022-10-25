class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def bs(temp, left, right):
            #print(temp, left, right)
            if left > right:
                return False
            
            pivot = (left + right) // 2
            
            if temp[pivot] == target:
                return True
            
            if temp[pivot] > target:
                return bs(temp, left, pivot - 1)
                
            if temp[pivot] < target:
                return bs(temp, pivot + 1, right)
                
        
        for i in range(len(matrix)):
            #print(matrix[i], 0, len(matrix[i]) - 1)
            if bs(matrix[i], 0, len(matrix[i]) - 1):
                return True
        
        else:
            return False