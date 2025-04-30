class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            p1, p2, count = i, i, 1
            for j in range(min(i, len(s)-i-1)):
                p1 -= 1
                p2 += 1
                if s[p1] != s[p2]:
                    if len(longest) < len(s[p1+1:p2]):
                        longest = s[p1+1:p2]
                    break
                elif p1 == 0 or p2 == len(s)-1:
                        if len(longest) < len(s[p1:p2+1]):
                            longest = s[p1:p2+1]

        for i in range(len(s)-1):
            p1, p2 = i, i+1
            if s[i] == s[i+1]:
                if len(longest) == 1:
                    longest = s[i:i+2]
                for j in range(min(i, len(s)-i-2)):
                    p1 -= 1
                    p2 += 1
                    if s[p1] != s[p2]:
                        if len(longest) < len(s[p1+1:p2]):
                            longest = s[p1+1:p2]
                        break
                    elif p1 == 0 or p2 == len(s)-1:
                        if len(longest) < len(s[p1:p2+1]):
                            longest = s[p1:p2+1]

        return longest
                    
