class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        If they aren't the same length, immediately return False. If they are, create two dictionaries one and two. Then enumerate through s and put the 
        letters in dicitonaries, both seperate, so one has the letters of t and two has the letters of s. Then if they are the same dictionary, return True 
        """
        if len(s) != len(t):
            return False
        one, two = {}, {}
        for i, a in enumerate(s):
            if t[i] not in one:
                one[t[i]] = 1
            else:
                one[t[i]] += 1
            if a not in two:
                two[a] = 1
            else:
                two[a] += 1
        if one == two:
            return True
        return False
