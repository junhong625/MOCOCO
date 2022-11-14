class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 단순히 전체가 넘어가면 절대 성립 안될 조건임
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        # 진행해 보면서 한곳에서 막히면 이전의 장소들도 모두 시작지점으로 할당할 수 없다는 것이 분명하다
        # 따라서 이후의 지점을 시작지점으로 재할당, 반복문을 진행해 나가자
        for i in range(len(gas)):
            if tank + gas[i] < cost[i]:
                start = i+1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        return start
            