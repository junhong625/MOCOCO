class Solution:
    def findKthLargest(self, nums, k) -> int:
        import heapq
        
        ## 첫번째 해결 방법 (Runtime: 866ms, Memory: 33.1MB)
        ## heappush를 활용하여 리스트를 최대 힙으로 변경하여 해결
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))
        
        for _ in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)[1]

        ## 두번째 해결 방법 (Runtime: 729ms, Memory: 26.3MB)
        ## 최소힙을 활용하되 최대길이에서 k(목표로 하는 순번)만큼 pop을 한 다음으로 pop한 숫자로 정답 출력
        # heapq.heapify(nums)
        # for _ in range(len(nums)-k):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)