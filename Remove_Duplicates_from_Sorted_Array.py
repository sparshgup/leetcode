class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        pos = 0
        
        for i in range(1, len(nums)):
            if nums[pos] == nums[i]:
                continue
            else:
                pos += 1
                nums[pos] = nums[i]        
        return pos + 1
