class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        amount = nums.count(0)
        for i in range(amount):
            nums.remove(0)
        nums.extend([0]*amount)