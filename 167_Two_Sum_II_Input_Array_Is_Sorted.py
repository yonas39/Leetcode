class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds and returns a pair of indices in the input list 'numbers' whose corresponding
        elements add up to the given 'target' value.

        Args:
            numbers (List[int]): A list of integers.
            target (int): The target sum value.

        Returns:
            List[int]: A pair of indices [index1, index2] such that numbers[index1] + numbers[index2] == target.

        Example:
            >>> solution = Solution()
            >>> solution.twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """

        
        lower = 0
        higher = len(numbers)-1

        while lower <= higher:
            if numbers[lower] + numbers[higher] == target:
                return [lower+1, higher+1]
            elif numbers[lower] + numbers[higher] > target :
                higher -= 1
            else:
                lower +=1
            
