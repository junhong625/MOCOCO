class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # 단순 탐색을 통한 counting
        # 이경우 시간이 기존보다 2배 가까이 걸리게 된다. 다만 메모리는 적게 쓴다
        count = 0
        gems = list(set(list(jewels)))
        # print(gems)
        for i in gems:
            for j in stones:
                if i == j:
                    count += 1
        return count

        # 딕셔너리를 활용한 counting
        # 적은 반복으로 빠른 속도가 장점
        count = {}
        for i in stones:
            count[i] = count.get(i, 0) + 1
        result = 0
        for i in jewels:
            result += count.get(i, 0)
        return result

