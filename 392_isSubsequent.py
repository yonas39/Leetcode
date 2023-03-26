class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ############## Solution 1 ##################
        # count=0
        # for char in t:
        #     if count < len(s) and s[count]==char:
        #         count+=1
        
        # return count == len(s)

        ############# Solution 2 ###################
        s_count=0
        t_count=0

        while s_count < len(s) and t_count < len(t):
            if s[s_count] == t[t_count]:
                s_count+=1
            t_count+=1
        return s_count == len(s)
