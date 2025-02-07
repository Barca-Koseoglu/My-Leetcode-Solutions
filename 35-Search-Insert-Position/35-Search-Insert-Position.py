class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        This program uses two pointers to do binary search on a sorted array.
        """
        left, right = 0, len(nums)-1

        while right >= left:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return left
        
