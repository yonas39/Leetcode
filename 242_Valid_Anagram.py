class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

        :param s: First input string.
        :param t: Second input string.
        :return: True if the strings are anagrams, False otherwise.
        """
        # Solution - 1
        # Convert strings to lists and sort them
        # s_temp = list(s)
        # t_temp = list(t)
        # s_temp.sort()
        # t_temp.sort()
        # Return comparison of sorted lists
        # return s_temp == t_temp

        # Solution - 2
        # Check if lengths of strings are equal
        if len(s) != len(t):
            return False

        count_s = {}  # Dictionary to store character counts for string s
        count_t = {}  # Dictionary to store character counts for string t

        # Count character occurrences in both strings
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # Compare the character counts of both strings
        return count_s == count_t
