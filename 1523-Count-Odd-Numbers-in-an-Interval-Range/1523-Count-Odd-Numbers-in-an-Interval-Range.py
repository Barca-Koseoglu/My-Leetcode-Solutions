class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 == 1 and high%2 == 1:
            return int((high-low+2)/2)
        if low%2 == 1 or high%2 == 1:
            return int((high-low+1)/2)
        else:
            return int((high-low)/2)
