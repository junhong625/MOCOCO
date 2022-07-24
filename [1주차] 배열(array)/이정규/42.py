class Solution(object):
    def trap(self, height):
        max,  idx, water = 0, 0, 0
        for i in range (len(height)) :
            if height[i] > max :
                max = height[i]
                idx = i
        
        compare = 0
        for i in range(idx + 1) :
            if compare < height[i] :
                compare = height[i]
            water += compare - height[i]
        
        compare = 0
        for i in range(len(height)-1, idx, -1) :
            if compare < height[i] :
                compare = height[i]
            water += compare - height[i]
        return(water)        