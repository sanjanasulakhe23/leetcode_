class Solution(object):
    def maxSubArray(self, nums):
        current_sum=0
        max_sum=float('-inf')
        for i in range(len(nums)):
            current_sum+=nums[i]
            max_sum=max(current_sum,max_sum)
            if current_sum<0:
                current_sum=0
        return max_sum    