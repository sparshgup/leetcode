class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return len(nums)
        
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[pos] = nums[i]
                pos += 1
                
        return pos
