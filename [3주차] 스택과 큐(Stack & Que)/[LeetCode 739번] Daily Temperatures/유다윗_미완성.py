class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        result = []
        for i in range(len(T)): # 온도 순회
            days = 1
            for j in range(i+1, len(T)): # 위에서 선택된 온도의 다음 온도부터 하나씩 순회
                if T[j] > T[i]: # j번째 온도가 i번째 온도보다 더 높을 경우
                    result.append(days)
                    break
                else:
                    days += 1
            else: # break가 안 걸린 경우, 즉 더 높은 온도가 없을 경우
                result.append(0)
        return result
    
    ##################################
    ######### 시간 초과 발생 ##########
    ##################################

    