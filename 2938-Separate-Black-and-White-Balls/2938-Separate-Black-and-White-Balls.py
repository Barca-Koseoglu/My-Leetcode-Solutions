class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        This is a very simple problem. To solve it, I just thought about parsing through each element in the string (reversed) and if that
        element is "1", aka the black ball, I would simply find out the number of steps it takes by subtracting the element's index by the 
        "count" variable. The "count" variable keeps track of the numbers of black balls in the right-most position. Any time a black ball
        is encountered, calculate the amount of steps required then add 1 to "count", because the count of the black balls in their correct position
        would increase by 1 after moving the black ball. Add all the values to the return variable, then return it.
        """
        ans, count = 0, 0
        s = s[::-1]
        for i, a in enumerate(s): 
            if a == "1":
                ans += i-count
                count += 1
        return ans
