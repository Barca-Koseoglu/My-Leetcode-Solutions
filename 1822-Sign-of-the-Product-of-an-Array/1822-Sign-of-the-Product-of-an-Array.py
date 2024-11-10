class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Iterate through the list. If zero is in there, immediately return 0. Otherwise count the amount of negative numbers. If there's a positive amount, 
        return 1 otherwise return -1.
        """
        negs = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negs += 1
        if negs%2 == 0:
            return 1
        else:
            return -1
