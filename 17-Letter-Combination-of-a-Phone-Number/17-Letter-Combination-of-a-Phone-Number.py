class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Create a dictionary that maps each number to a tuple of it's values. Then the function comb takes x, the index of digits, and count, the current 
        combination of digits as a string. if x is bigger than the length of digits, then exit out of the current recursion. Otherwise, run a for loop 
        through here[digits[x]], which is the tuple of values of the current number. Add the iteration to count, then recursively run comb again with x+1 and 
        the current count until the length of count is the length of digits. Once it is, append it onto the return variable, then remove the latest letter in 
        the string to replace it with the next iteration. After many runs of this, return the list of combinations.
        """
        ans = []
        here = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z")
        }
        
        def comb(x, count):
            if x == len(digits):
                return False
            for i in here[digits[x]]:
                count += i
                comb(x+1, count) # recursion
                if len(count) == len(digits):
                    ans.append(count)
                count = count[:-1]
        comb(0, "")
        return ans
