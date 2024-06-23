class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
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
        """
        count = 0
        for i in range(len(nums)):
            if nums[i-count]%2 == 1:
                nums.append(nums[i-count])
                del nums[i-count]
                count += 1
        return nums