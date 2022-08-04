class Solution(object):
    def trap(self, height):
        max_height, max_idx, total = max(height), 0, 0
        
        # 최대값의 인덱스를 찾는 반복문
        for i in range(len(height)):
            if max_height == height[i]:
                max_idx = i
                break # 최댓값의 인덱스를 찾을 경우 break문을 통해 시간 단축
        # 기준값
        default_value = 0
        # 시작부터 최댓값까지의 물 크기를 찾아서 더하는 반복문
        for h in height[:max_idx+1]:
            if h > default_value:
                default_value = h
            # 같을 경우 pass 하는 것으로 시간 단축
            elif h == default_value:
                pass
            else:
                total += default_value - h
        
        default_value = 0
        # 끝부터 최댓값까지의 물 크기를 찾아서 더하는 반복문
        for h in height[-1:max_idx:-1]:
            if h > default_value:
                default_value = h
            # 같을 경우 pass 하는 것으로 시간 단축
            elif h == default_value:
                pass
            else:
                total += default_value - h
        return total