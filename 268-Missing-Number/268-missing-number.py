class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checkmate = (len(nums) * (len(nums)+1))//2
        
        return checkmate - sum(nums)
