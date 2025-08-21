class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        total=0
        prefix_map={0:1}
        for num in nums:
            total+=num
            if total-k in prefix_map:
                count+=prefix_map[total-k]
            prefix_map[total]=prefix_map.get(total,0)+1

        return count        
            