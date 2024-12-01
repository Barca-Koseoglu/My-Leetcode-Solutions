class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = inf
        for i in range(len(nums)):
            top = 0

            for j in range(i, len(nums)):
                top += nums[j]

                if l <= j-i+1 <= r:
                    ans = top if (top < ans) and (top > 0) else ans
        
        return ans if ans != inf else -1
