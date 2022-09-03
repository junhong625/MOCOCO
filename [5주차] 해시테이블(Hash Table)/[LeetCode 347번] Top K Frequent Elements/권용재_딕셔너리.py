class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 딕셔너리 만들기
        MAP = {}
        # 키값
        keys = set(nums)
        # 키값에 대한 value 초기화
        for key in keys:
            MAP[key] = 0
        # value 넣기
        for i in nums:
            MAP[i] +=1
        
        # 정렬해서 새로운 리스트로 받기 (key, value) 형태로
        sort_list = sorted(MAP.items(), key=lambda x: x[1], reverse=True)
        
        # 정답 구하기
        result = []
        for i in range(k):
            result.append(sort_list[i][0])

        return result