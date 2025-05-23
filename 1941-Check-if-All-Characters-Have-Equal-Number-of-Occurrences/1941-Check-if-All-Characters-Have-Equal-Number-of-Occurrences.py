class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        check = count[s[0]]
        for i in count.values():
            if i != check:
                return False
        return True
      
