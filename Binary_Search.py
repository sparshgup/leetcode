class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right = len(nums)-1
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
