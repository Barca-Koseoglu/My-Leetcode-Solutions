class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        if len(count) == 1:
            return 'equilateral'
        elif len(count) == 2:
            for i in count:
                if count[i] == 2:
                    two = i
                else:
                    one = i
            if two*2 > one:
                return 'isosceles'
            return 'none'
        else:
            check = sum(nums)
            if check-nums[0] > nums[0] and check-nums[1] > nums[1] and check-nums[2] > nums[2]:
                return 'scalene'
            return 'none'
