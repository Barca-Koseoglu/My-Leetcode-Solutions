class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Find the first non-zero difference between two consecutive numbers. Then iterate through the list to see if the number before the current iteration 
        is the same sign as the first different using boolean values, True for positive and False for negative. If the numbers are the same, just continue. 
        If the difference is the opposite sign, return False. If you exit the for loop, return True.
        """
        if len(nums) < 3: # edge case 1
            return True
        p2 = 1
        while nums[p2] == nums[0]: # edge case 2
            p2 += 1
            if p2 >= len(nums)-1:
                return True
        if nums[p2] - nums[0] > 0:
            check = True
        else:
            check = False
        for i in range(p2+1, len(nums)):
            if nums[i] - nums[i-1] > 0 and check == False:
                return False
            if nums[i] - nums[i-1] < 0 and check == True:
                return False
        return True
