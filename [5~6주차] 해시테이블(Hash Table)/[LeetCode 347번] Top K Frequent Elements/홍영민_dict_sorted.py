import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 속도가 매우 빠른 편에 속한다
        # 딕셔너리에 다 넣어주고, sorted를 활용해서 뽑아낼 순서대로 앞에 서 찾아내면 된다.
        # 심지어 딕셔너리가 리스트로 변환되어 조회하기도 편안
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        # 위의 두줄은 counter로 더 줄여버릴 수 있다
        sort_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            key, value = sort_list[i]
            result.append(key)
        return result

