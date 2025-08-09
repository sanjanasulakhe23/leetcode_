class Solution(object):
    def longestConsecutive(self, nums):
        longest_length=0
        hashmap={}
        for num in nums:
            hashmap[num]=False
        for num in nums:
            current_length=1

            next_num=num+1
            while next_num in hashmap and not hashmap[next_num]:
                current_length+=1
                hashmap[next_num]=True
                next_num+=1
            prev_num=num-1    
            while prev_num in hashmap and not hashmap[prev_num]:
                current_length+=1
                hashmap[prev_num]=True
                prev_num-=1

            longest_length=max(longest_length,current_length) 
        return longest_length                   