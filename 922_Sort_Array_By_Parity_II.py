class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
            Rearranges the elements of the input list 'nums' such that all even numbers
            appear at even indices and all odd numbers appear at odd indices.

            Args:
                nums (List[int]): A list of integers.

            Returns:
                List[int]: The modified list with the elements rearranged.

            Example:
                >>> solution = Solution()
                >>> solution.sortArrayByParityII([4, 2, 5, 7])
                [4, 5, 2, 7]
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1

        output = []
        size = len(nums)-1
        for i in range(len(nums)//2):
            output.append(nums[i])
            output.append(nums[size-i])
        return output
