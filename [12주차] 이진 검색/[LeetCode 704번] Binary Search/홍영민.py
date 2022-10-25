class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 오름차순으로 정렬 되어 있으니, 크기 비교 가능
        self.result = -1
        def binary(left,right):
            if left+1 == right or left==right:
                if nums[left] == target:
                    self.result = left
                    return
                elif nums[right] == target:
                    self.result = right
                    return
                else:
                    return
            n = (left + right)//2
            if nums[n] == target:
                self.result = n
                return
            elif nums[n] > target:
                binary(left,n)
            elif nums[n] < target:
                binary(n,right)
        # 수정본. 이것이 더 확실하다
        def binary(left,right):
            if left > right:
                return
            n = (left + right)//2
            if nums[n] == target:
                self.result = n
                return
            elif nums[n] > target:
                binary(left,n-1)
            elif nums[n] < target:
                binary(n+1,right)
        binary(0,len(nums)-1)
        return self.result