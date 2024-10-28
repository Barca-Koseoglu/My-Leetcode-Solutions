class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        I really liked this question. At first I thought the question was asking me to use the consecutive subsequences of the sorted array,
        but I quickly realized I was mistaken. So to solve this problem, I first and formost made a variable "check" which contained the hash set of the
        original array. Then, I looped over the original array and checked if the square root of the number was in the set. If it was, I would set "i" to the
        square root and increase the "count" variable by 1, which just keeps track of the length of the sequence. If there is no other square root of "i", 
        I see if "count" is the longest sequence by comparing it with the return variable "ans". If it's bigger, set "ans" to "count", or else continue. 
        After everything, if "ans" is equal to 1 (default value; no sequence of square roots), return -1, or else return "ans".
        """
        check = set(nums) # hash set of nums
        ans = 1 # return var
        for i in nums:
            count = 1 # len of sequence tracker starting at 1
            while (i**.5)%1 == 0 and i**.5 in check: # to see if there are square roots of numbers in nums
                count += 1
                i = i**.5 # set i to the square root and repeat the loop
            if count > ans:
                ans = count # see if count is the biggest so far
        if ans == 1:
            return -1
        return ans
