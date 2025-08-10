class Solution(object):
    def threeSum(self, nums):
        if nums is None or len(nums)<3:
            return []

        nums.sort()

        result=set()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1

            while left<right:
                target=nums[i]+nums[left]+nums[right]

                if target==0:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif target<0:
                    left+=1
                elif target>0:
                    right-=1
        return list(map(list,result))                

            
       