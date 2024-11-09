class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Take the biggest number in the list, the iterate through it. If adding the extra candies to the current iteration is bigger than or equal to the 
        biggest number, then append True to the return variable. Otherwise, append False.
        """
        max_candies = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
