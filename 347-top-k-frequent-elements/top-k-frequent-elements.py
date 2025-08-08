class Solution(object):
    def topKFrequent(self, nums, k):
        bucket=[[] for _ in range(len(nums)+1)]
        frequency_map={}


        for n in nums:
            if n not in frequency_map:
                frequency_map[n]=1
            else:    
                frequency_map[n]+=1

        for key,frequency in frequency_map.items():
            bucket[frequency].append(key)

        result=[]

        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for value in bucket[i]:
                    if len(result)<k:
                        result.append(value)
                    else:
                        return result
        return result                        