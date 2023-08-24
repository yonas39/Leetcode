class Solution:
  def groupAnagrams(self, strs):
      """
      Group a list of strings such that each group consists of anagrams of each other.
      
      Args:
      - strs (List[str]): List of strings to be grouped.
      
      Returns:
      - List[List[str]]: List of grouped anagrams.
      """
      
      # Dictionary to store groups of anagrams
      anagram_groups = {}
      
      # Iterate over each string
      for s in strs:
          # Use sorted string as key (tuple since lists are unhashable)
          key = tuple(sorted(s))
          # Add the string to the appropriate group
          if key in anagram_groups:
              anagram_groups[key].append(s)
          else:
              anagram_groups[key] = [s]
      
      # Return the grouped anagrams
      return list(anagram_groups.values())
  
  # Test
  print(groupAnagrams(["eat", "tea", "tan", "ant", "bat"])) 
  # Expected: [['eat', 'tea'], ['tan', 'ant'], ['bat']]
