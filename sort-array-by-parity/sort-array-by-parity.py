class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        even.extend(odd)
        return even