class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This algorithm utilizes a dictionary to find two numbers that add up to a target number.
        """
        store = {}
        
        for i, a in enumerate(nums):
            if target - a in store:
                return [i, store[target - a]]
            store[a] = i
        
