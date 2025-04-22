class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        high, low = 0, 0
        x = 0
        for i in differences:
            x += i
            high = max(high, x)
            low = min(low, x)

        return max(0, upper - lower - high + low + 1)
