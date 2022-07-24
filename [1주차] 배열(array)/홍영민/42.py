class Solution(object):
    
    def trap(self, height):
        # 숫자 변화 함수
        def change(height, x, y, count = 1):
            higher = 0
            for i in range(x,y,count):
                if height[i] > higher:
                    higher = height[i]
                else :
                    height[i] = higher
            return height
        # 전체 면적 - 기존 벽 면적으로 결과값을 계산할 것이다
        pillar = sum(height)
        # 최고점을 찾아내서 그 중간은 동일 높이로, 이외에는 계단식으로 계산
        max_height = max(height)
        high_points = [i for i, x in enumerate(height) if x == max_height]
        
        for i in range(high_points[0], high_points[-1]):
            height[i] = max_height
            
        change(height, 0, high_points[0])
        # 반대쪽도 대칭으로 계산
        change(height, len(height)-1, high_points[-1], count = -1)

        return sum(height) - pillar
            
        
        
# stack 활용한 샘플 코드       
#     def trap(self, height):
#         stack = []
#         volume = 0
#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]:
#                 print(stack,volume)
#                 top = stack.pop()
#                 if not len(stack):
#                     break
                
#                 distance = i - stack[-1] -1
#                 waters = min(height[i], height[stack[-1]]) - height[top]
                
#                 volume += distance * waters
#             stack.append(i)
#         return volume