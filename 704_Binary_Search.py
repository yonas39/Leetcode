class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # define min and max values as left and right 
        left = 0
        right = len(nums)-1

        # loop until left is less than or equal to right 
        while left<=right:
  
            mid = (left+right)//2 #find the mid point using integer division
            
            if nums[mid] == target: # if the number is found return the index 
                return mid
            elif nums[mid]<target: # if target is greater move one step up from the left
                left=mid+1
            elif nums[mid]>target: # if taget is lowesr move one step down from the right 
                right=mid-1

        return -1 
                
