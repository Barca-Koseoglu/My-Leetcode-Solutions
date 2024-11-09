class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Make a set called check with all the lowercase and uppercase vowels in it. Then convert the string s to a list and make two pointers p1 and p2 set to 
        0 and the length of the list minus one respectively. Then while p2 is bigger than p1, check if s[p1] and s[p2] isn't in check. If they aren't, add 1 
        to p1 and subtract 1 from p2. If they both are in check, then swap them and also add 1 to p1 and subtract 1 from p2. After p2 is smaller than or 
        equal to p1, meaning it has gone to the left of p1, exit out of the loop and return s as a string.
        """
        check = set(['a', "A", 'e', "E", 'i', "I", 'o', "O", 'u', "U"])
        s = list(s)
        p1, p2 = 0, len(s)-1
        while p2 > p1:
            if s[p1] not in check:
                p1 += 1
            if s[p2] not in check:
                p2 -= 1
            if s[p1] in check and s[p2] in check:
                replace = s[p1]
                s[p1] = s[p2]
                s[p2] = replace
                p1 += 1
                p2 -= 1
        return "".join(s)
