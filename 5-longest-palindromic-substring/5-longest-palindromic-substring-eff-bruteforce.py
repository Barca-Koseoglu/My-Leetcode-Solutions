class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_check(string):
            p1, p2 = 0, len(string)-1
            while p1 < p2:
                if string[p1] != string[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True
                
        
        for i in range(len(s), -1, -1):
            for j in range(len(s)-i+1):
                if palindrome_check(s[j:i]):
                    return s[j:i]
                i += 1
              
