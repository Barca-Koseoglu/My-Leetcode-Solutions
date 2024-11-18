class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        """
        Create a set called count. Iterate through the array except the last index. If the index you're on plus the next is in the set, return true, 
        otherwise add it to the set. If you exit the loop, return False.
        """
        count = set()
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] in count:
                return True
            count.add(nums[i]+nums[i+1])
        return False
