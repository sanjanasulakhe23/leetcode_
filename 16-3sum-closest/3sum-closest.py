class Solution(object):
    def threeSumClosest(self, nums, target):
        n=len(nums)
        closest_sum=float('inf')
        nums.sort()
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                elif current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return current_sum
        return closest_sum                        