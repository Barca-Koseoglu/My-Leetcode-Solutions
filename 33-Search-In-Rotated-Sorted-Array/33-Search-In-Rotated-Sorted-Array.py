class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            midpoint = (left+right)//2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] >= nums[left]:
                if nums[left] <= target and nums[midpoint] > target:
                    right = midpoint-1
                else:
                    left = midpoint+1
            else:
                if nums[midpoint] < target and nums[right] >= target:
                    left = midpoint+1
                else:
                    right = midpoint-1
        return -1
        
