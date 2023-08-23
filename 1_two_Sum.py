class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find and return indices of two numbers in the list that add up to the target.

        :param nums: List of integers.
        :param target: Target sum.
        :return: List of two indices [index1, index2] where the elements at these indices sum up to the target.
        """
        hash_map = {}  # Dictionary to store seen numbers and their indices

        for i in range(len(nums)):
            diff = target - nums[i]  # Calculate the difference between target and current number
            if diff in hash_map:
                return [hash_map[diff], i]  # Return indices if the difference is in the hash_map
            hash_map[nums[i]] = i  # Store current number in the hash_map with its index
        
        # If no solution found, an empty list can be returned or an exception can be raised
        # return []  # Return an empty list if no solution found
        # raise ValueError("No solution found")  # Raise an exception if no solution found
