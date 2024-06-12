class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        for i in nums:
            digits = len(str(i))
            if digits%2 == 0:
                final += 1
        return final