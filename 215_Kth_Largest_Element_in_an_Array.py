"""
215. Kth Largest Element in an Array
Medium
14.4K
706
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
####################################################################################
##################### Solution #####################################################
####################################################################################

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in a list of numbers.

        Args:
            nums (List[int]): The list of numbers.
            k (int): The position of the element to find (1-based index).

        Returns:
            int: The kth largest element.

        Example:
            >>> solution = Solution()
            >>> nums = [3, 1, 4, 2, 5]
            >>> k = 2
            >>> solution.findKthLargest(nums, k)
            4
        """

        nums.sort(reverse=True)
        return nums[k-1]
            
            
