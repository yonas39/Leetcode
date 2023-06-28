class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Original solution using two separate lists for even and odd numbers
        # even = []  # List to store even numbers
        # odd = []   # List to store odd numbers
        # Iterate over each number in the given list
        # for num in nums:
        #     # Check if the number is even
        #     if num % 2 == 0:
        #         even.append(num)  # Add even number to the even list
        #     else:
        #         odd.append(num)   # Add odd number to the odd list
        # return even + odd  # Combine even and odd lists to get the sorted array

        ########### Alternative Solution ##############
        j = 0
        # Iterate over each index in the range of the given list
        for i in range(len(nums)):
            # Check if the number at the current index is even
            if nums[i] % 2 == 0:
                # Swap the number at index i with the number at index j
                nums[i], nums[j] = nums[j], nums[i]
                j += 1  # Increment j to move it to the next available position for even numbers
        return nums  # Return the modified list containing the sorted array
