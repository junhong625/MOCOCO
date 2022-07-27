class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_idx = 0                                              #시작 포인터
        right_idx = len(height)-1                                 #끝 포인터 
        left_max, right_max = height[left_idx], height[right_idx] #양쪽 포인터의 최대 높이 변수 & 초기값 설정
        volume = 0                                                #물의 양 default
        
        while left_idx < right_idx:                               #최대 높이 인덱스에 도달했을 때 멈춘다
            left_max = max(left_max, height[left_idx])            #인덱스의 높이 최댓값이 바뀔 경우 최댓값 새로 저장
            right_max = max(right_max, height[right_idx])
            
            if left_max < right_max:
                volume += left_max - height[left_idx]             #높이가 낮아진 만큼 물을 채움
                left_idx += 1
            else:
                volume += right_max - height[right_idx]           #오른쪽에서 시작해서 낮아진 만큼 물을 채움
                right_idx -= 1
                
        return volume