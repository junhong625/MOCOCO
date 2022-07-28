

############ 실패작 ################### 추후 다시 도전하겠습니다....

class Solution:
    def trap(self, height) -> int:
    
        result = 0
        ip_stack = {0:height[0]} # key:index, value:height
        idx_list = []
        
        for idx, i in enumerate(height[1:], 1):
            left_idx = None
            
            # 현재 인덱스에서의 높이가 이전 인덱스의 높이보다 높을 경우(변곡점)
            if i > height[idx-1]:
                
                if max(ip_stack.values()) == height[idx-2]:
                    left_idx = idx-2
                else:
                    height_rv = height[:idx][::-1]
                    left_idx = len(height_rv) - height_rv.index(max(ip_stack.values())) -1

                b = idx - left_idx - 1
                h = min(i, height[left_idx])
                
                print(b, h)
                area = b * h
                huddles = 0
                for j in height[left_idx+1: idx]:
                    if j > h:
                        huddles += h
                    else:
                        huddles += j
            
                area = area - huddles
                
                for j in idx_list:
                    if left_idx <= j[0] and i > height[j[1]]:
                        print(f'인덱스 {idx}에서 통과')
                        area -= j[2]
                
                result += area

                ip_stack.update({idx: i})
                idx_list.append([left_idx, idx, area])

            
        return result