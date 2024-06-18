class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i-count] == nums[i-count-1]:
                del nums[i-count-1]
                count += 1
        return len(nums)
        