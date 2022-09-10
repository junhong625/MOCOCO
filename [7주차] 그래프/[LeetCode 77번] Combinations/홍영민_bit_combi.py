class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 비트 연산자를 통한 부분집합
        # 다만, 최악의 효율을 보여주고 있었다 (하위 5%)
        result = []
        for i in range(1<<n):
            subset = []
            for j in range(n):
                if i & 1<<j:
                    subset.append(j+1)
            if len(subset) == k:
                result.append(subset)
        return result

        # 참고로 아래의 것을 활용하면 쉽게 생성가능
        return list(itertools.combinations(range(1,n+1),k))
