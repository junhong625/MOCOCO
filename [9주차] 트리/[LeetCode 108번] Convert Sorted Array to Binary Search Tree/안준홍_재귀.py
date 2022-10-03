class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:            # 존재하지 않을 경우 종료
            return
        center = len(nums)//2   # 중간 값을 루트로 배정하기 위함과 동시에 left, right값을 분할해주는 기준이 되는 변수
        return TreeNode(nums[center], self.sortedArrayToBST(nums[:center]), self.sortedArrayToBST(nums[center+1:]))