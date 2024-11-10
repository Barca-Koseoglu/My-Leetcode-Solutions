class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Make a dictionary called store and store the numbers of letters in s. Then iterate through i and if it isn't in store, return that value. If it is 
        but the amount of that letter in store is 0, then also return that value.
        """
        store = {}
        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        for i in t:
            if i in store:
                if store[i] == 0:
                    return i
                store[i] -= 1
            else:
                return i
    
