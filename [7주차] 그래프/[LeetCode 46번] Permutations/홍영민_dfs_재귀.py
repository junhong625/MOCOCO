class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visit = [0]*len(nums)
        result = []
        def dfs(stack,visited):
            if len(stack) == len(nums):
                # 두번째는 깊은 복사를 통해서 출력해야 한다. 이렇지 않으면 저장된 stack이 마지막으로 입력된 값으로 초기화된다.
                result.append(stack[:])
                return
            else:
                for idx, i in enumerate(visited):
                    if i == 0:
                        stack.append(nums[idx])
                        visited[idx] = 1
                        dfs(stack, visited)
                        # 우선, 앞의 숫자를 없애줘야 반복문에서도 돌아가게 만들 수 있다
                        # visited 를  0으로 되돌리는 점에서 확인할 수 있다.
                        stack.pop()
                        visited[idx] = 0
        dfs([],visit)
        return result