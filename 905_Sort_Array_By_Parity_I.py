class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
                """
        Rearranges the elements of the input list 'nums' such that all even numbers
        appear before all odd numbers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: The modified list with the elements rearranged.

        Example:
            >>> solution = Solution()
            >>> solution.sortArrayByParity([4, 2, 5, 7])
            [4, 2, 5, 7]
        """

        # even=[]
        # odd =[]
        # for num in nums:
        #     if num%2==0:
        #         even.append(num)
        #     else:
        #         odd.append(num)
        # return even+odd

        ########### Alternative Solution ##############
        j = 0
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        return nums
