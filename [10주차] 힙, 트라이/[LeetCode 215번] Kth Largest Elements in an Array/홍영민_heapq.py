import heapq
class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapq를 활용한 반복해서 pop, 다만 이 경우 timelimit이 뜬다
        # 따라서 역순으로 접근하는 방식이 필요하다
        for i in range(len(nums)-k+1):
            heapq.heapify(nums)
            i = heapq.heappop(nums)
        return i
    
    # 교재 내의 heap 구현 수도코드를 가져와서 조절해 보았다
    def findKthLargest(self, nums, k):
        nums = [0] + nums
        bank = []
        def up(ls,key):
            ls.append(key)
            i = len(ls)-1
            parent = i // 2
            while parent > 0 :
                if ls[i] > ls[parent]:
                    ls[parent], ls[i] = ls[i],ls[parent]
                i = parent
                parent = i // 2
        for i in nums:
            up(bank, i)
        def down(idx):
            left = idx * 2
            right = idx * 2 + 1
            smallest = idx
            
            if left <= len(bank)-1 and bank[left] > bank[smallest]:
                smallest = left
            if right <= len(bank)-1 and bank[right] > bank[smallest]:
                smallest = right
            if smallest != idx:
                bank[idx], bank[smallest] = bank[smallest], bank[idx]
                down(smallest)
        def extract(ls):
            extracted = ls[1]
            ls[1] = ls[len(ls)-1]
            ls.pop()
            down(1)
            return extracted
            
        for i in range(k):
            result = extract(bank)
        return result