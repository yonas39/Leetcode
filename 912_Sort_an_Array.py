class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers nums, sort the array in ascending order and return it.

        You must solve the problem without using any built-in functions in O(nlog(n)) time complexity   and with the smallest space complexity possible.
        """
        
        # I used merge sort 
        
        if len(nums)<=1: 
            return nums
        
        # Divide the array into two (half way)
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        
        # Recursively sort the left and right arrays 
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)
        
        
        i=j=0
        merged_list=[] #new list to contain the sorted list 
        
        while i < len(left_sorted) and j < len(right_sorted): 
            if left_sorted[i] < right_sorted[j]:
                merged_list.append(left_sorted[i])
                i+=1
            # elif right_sorted[i] > left_sorted[j]:
            else:
                merged_list.append(right_sorted[j])
                j+=1
        
        # if any value remain in the left or right array merge it to the out put 
        merged_list+= left_sorted[i:] or right_sorted[j:]
#         merged_list+= right_sorted[j:]

        return merged_list
