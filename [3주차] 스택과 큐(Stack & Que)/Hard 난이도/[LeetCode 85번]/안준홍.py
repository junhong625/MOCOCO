'111111011111111'
'101101111111111'
'111111111111111'
'011111101110111'
'100111111110111'
'111111111111111'
'111011111110111'
'111100011111010'
'101100011110101'
'101111110111011'
'101111111111111'
'111011111111111'
'111000101111111'
'111111011111111'
'111111101111101'

class Solution(object):
    def maximalRectangle(self, matrix):
        from collections import deque
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        stack_idx = deque()
        max_val = 0
        for row in range(len(matrix)):
            for num in range(len(matrix[0])):
                
                if matrix[row][num] == '1':
                    stack_idx.append(num)
                if matrix[row][num] == '0' or num == len(matrix[0])-1:
                    max_val = max_val if max_val > len(stack_idx) else len(stack_idx)
                    cnt = 0
                    # print(stack_idx)

                    # row+1을 체크하는 파트
                    if stack_idx and row+1 < len(matrix):
                        # print(row+1< len(matrix))
                        while True:
                            if stack_idx and matrix[row+1][stack_idx[0]] == '0':
                                stack_idx.popleft()
                            elif stack_idx and matrix[row+1][stack_idx[-1]] == '0':
                                stack_idx.pop()
                            else:
                                break
                        if stack_idx:
                            for i in matrix:
                                # if stack_idx:
                                    # print("".join(i[stack_idx[0]:stack_idx[-1]+1]), '1' * len(stack_idx))
                                if "".join(i[stack_idx[0]:stack_idx[-1]+1]) == '1' * len(stack_idx):
                                    cnt += 1
                                    max_val = max_val if max_val > cnt * len(stack_idx) else cnt * len(stack_idx)
                                else:
                                    cnt = 0
                    # row-1을 체크하는 파트
                    cnt = 0
                    if stack_idx and row-1 >= 0:
                        # print(row-1< len(matrix))
                        while True:
                            if stack_idx and matrix[row-1][stack_idx[0]] == '0':
                                stack_idx.popleft()
                            elif stack_idx and matrix[row-1][stack_idx[-1]] == '0':
                                stack_idx.pop()
                            else:
                                break
                        if stack_idx:
                            for i in matrix:
                                # if stack_idx:
                                    # print("".join(i[stack_idx[0]:stack_idx[-1]+1]), '1' * len(stack_idx))
                                if "".join(i[stack_idx[0]:stack_idx[-1]+1]) == '1' * len(stack_idx):
                                    cnt += 1
                                    max_val = max_val if max_val > cnt * len(stack_idx) else cnt * len(stack_idx)
                                else:
                                    cnt = 0




                    stack_idx = deque()
                    print(row, num, max_val)
        return max_val