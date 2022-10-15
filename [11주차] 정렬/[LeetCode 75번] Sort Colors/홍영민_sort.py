class Solution(object):
    # 어떤 정렬을 써도 다 풀리긴 하지만
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 버블정렬
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] >= nums[j]:
                    nums[j],nums[i] = nums[i],nums[j]
        return nums
    # 퀵정렬을 통해 중간값을 vector값으로 활용
    def sortColors(self,nums):
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[blue],nums[white] = nums[white], nums[blue]
            else:
                white += 1
        return nums
                