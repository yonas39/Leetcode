class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Check if there are duplicate elements within a distance of k in the given list.

        :param nums: List of integers.
        :param k: Maximum allowed distance between duplicate elements.
        :return: True if duplicate elements within distance k exist, False otherwise.
        """
        if k == 0:
            return False

        dic = {}  # Dictionary to store elements and their indices
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = 1
                if len(dic) > k:
                    dic.pop(nums[i - k])
        return False
