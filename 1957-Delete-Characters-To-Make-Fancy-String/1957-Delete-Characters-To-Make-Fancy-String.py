class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Use sliding window technique. Make 3 variables as pointers that start at the first three indices. If they aren't all equal, concatenate the value of 
        the smallest index to the return variable. if they are equal, just don't concatenate anything to the return variable. Then, add 1 to all the values. 
        Reapeat this using a while loop that stops when the biggest pointer reaches the end. After the while loop is finished, return the answer and 
        concatenate the first 2 pointers. If the length of s is less than 3, just return s.
        """
        if len(s) < 3: # edge case
            return s
        ans = ""
        p1, p2, p3 = 0, 1, 2 # pointers
        while p3 < len(s):
            if not(s[p1] == s[p2] == s[p3]): # check if 3 consecutive characters are equal
                ans += s[p1]
            p1 += 1
            p2 += 1
            p3 += 1
        return ans + s[p1] + s[p2] # concatenate because p1 and p2 become last 2 values after while loop ends
