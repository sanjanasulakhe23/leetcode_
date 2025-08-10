class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        maxarea=0
        while left<right:
            area=min(height[left],height[right])*(right-left)

            maxarea=max(area,maxarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea            
         
        