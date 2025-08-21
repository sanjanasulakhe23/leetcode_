class NumArray(object):

    def __init__(self, nums):
        self.prefix=[0]*len(nums)
        running=0
        for i ,num in enumerate(nums):
            running+=num
            self.prefix[i]=running
    def sumRange(self, left, right):
        if left==0:
            return self.prefix[right]
        
        return self.prefix[right]-self.prefix[left-1] 
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)