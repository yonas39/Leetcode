class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
            Given a string s which consists of lowercase or uppercase letters, return the length of 
            the longest palindrome that can be built with those letters.
        """
        result={}
        maximum = 0
        is_odd = False
        for char in s:
            if char in result:
                result[char] +=1
            else:
                result[char]=1
        
        for key, val in result.items():
            if val%2 == 0:
                maximum += val
            else:
                maximum += val-1
                is_odd = True
        if is_odd:
            maximum +=1
        return maximum 
