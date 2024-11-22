class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash map solution with O(n) time and space
        def hash_sol():
            made = {}

            for i in nums:
                if i in made:
                    made[i] += 1
                else:
                    made[i] = 1
        
            for i in made:
                if made[i] > len(nums)/2:
                    return i
        
        # Boyer-Moore Voting Algorithm solution with O(n) time and O(1) space
        def boyer_moore():
            count = candidate = 0

            for i in nums:
                if count == 0:
                    candidate = i
                
                if candidate == i:
                    count += 1
                else:
                    count -= 1
            
            return candidate
        

        return boyer_moore()
