# 처음에 작성했던 코드
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(temperatures)-1): ## 이중 for문을 통해 현재 인덱스부터 시작해 현재 온도보다 높은 온도를 가진 인덱스가 나올 때까지 반복
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]: ## 높은 온도를 가진 인덱스가 나올 경우 두 인덱스의 차이를 result에 추가
                    result.append(j-i)
                    break
            else:
                result.append(0) # 현재 온도보다 높은 온도를 찾지 못할 경우 0을 반환
        result.append(0)
        return result
# 위 코드를 통해 정답을 구할 수는 있지만 속도가 느려 Time Limit Exceeded에러가 났습니다.
# 속도를 높이고 stack을 이용하기 위해 stack에 현재 온도를 추가하는 방식을 택했습니다.
# for문을 통해 현재 idx의 온도를 추가하는데 추가하기 이전에 while문 안에서 stack의 마지막에 있는 온도와 현재의 온도를 비교하여 현재의 온도가 높을 경우
# 두 온도의 차이를 result에 추가하는 방식으로 구현해야겠다 생각했습니다.

# 시행 착오 결과 나온 정답 코드
# 현재 온도를 stack에 추가하는 방식을 택할 경우 현재 온도의 index를 구하기 어려웠습니다.
# 따라서 온도 대신에 index를 추가하여 해당 index를 이용하여 온도를 구하고 두 온도의 index 차이를 구하는 방식으로 구현했습니다.
class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(t) # 각 index에 온도가 높아지는 날과의 index 차이를 기록하기 위해 t 길이 만큼의 리스트 생성
        stack = [] # 스택의 역할을 할 리스트
        for idx in range(len(t)): # index 처음부터 끝까지 순회
            while stack and t[stack[-1]] < t[idx]: # stack에 원소가 존재하고 stack의 마지막 값인 index의 온도가 현재 index의 온도보다 낮을 경우
                result[stack[-1]] = idx-stack[-1] # result[stack[-1]]에 현재 index와 stack의 마지막 값(index)의 차이를 할당 
                stack.pop() # stack의 마지막 값 삭제
            stack.append(idx) # 현재 날짜 인덱스 추가
        return result