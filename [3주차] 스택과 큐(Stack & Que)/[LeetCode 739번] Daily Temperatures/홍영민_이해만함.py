class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp = []
        result = [0]*len(temperatures)
        for idx, today in enumerate(temperatures):
            # print(temp)
            while temp and today > temperatures[temp[-1]]:
                # 전날 또는 전전날에 비교해서 내가 상승했으면 그 날짜 차이를 계산해서 result에 넣어준다
                # 상승세면 인덱스가 하나씩 줄어든다, 하락세면 그냥 밑에 가서 붙는다(하루 증가)
                before = temp.pop()
                result[before] = idx - before
            # print(temp)
            # 일단 전날껄 무조건 넣는다
            temp.append(idx)
        return result

    ## 이전에 2중 for문으로 맞는 코드를 구현하긴했는데 시간초과가 났다. 이해가 안되서 그냥 해답을 보고 읽었다.
    # 사람이 어떻게 저렇게 생각하지