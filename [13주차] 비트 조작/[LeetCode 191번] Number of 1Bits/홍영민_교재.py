class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count('1')
        # bit를 하나씩 빼가는 과정은 자리수를 하나씩 앞에서 없애는 과정
        # &연산자를 통해 앞의 자리수만을 남겨준다
        # 결국, 1의 갯수 만큼 반복문이 돌아가게 된다
        count = 0
        while n:
            print(n)
            n &= n-1
            count += 1
        return count