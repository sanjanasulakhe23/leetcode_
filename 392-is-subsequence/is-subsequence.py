class Solution(object):
    def isSubsequence(self, s, t):
        itr1 ,itr2=0,0

        while itr1<len(s) and itr2 <len(t):
            if s[itr1]==t[itr2]:
                itr1+=1
                itr2+=1
            else:
                itr2+=1
        return itr1==len(s)            
        
        