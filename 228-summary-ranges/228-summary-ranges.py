class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges, holder = [], 0
        for i in range(len(nums)):
            if i - holder != nums[i] - nums[holder]:
                if holder == i - 1:
                    ranges.append(str(nums[holder]))
                else:
                    ranges.append(f'{nums[holder]}->{nums[i-1]}')
                holder = i

        if holder == len(nums) - 1:
            ranges.append(str(nums[holder]))
        else:
            ranges.append(f'{nums[holder]}->{nums[len(nums)-1]}')

        return ranges
      
