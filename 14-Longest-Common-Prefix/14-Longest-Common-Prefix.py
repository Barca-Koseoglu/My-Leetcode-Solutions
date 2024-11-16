class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        return variable count stores the current longest common prefix. Loop through the first word. For each letter, loop through every word except the 
        first. If the length of the word is smaller than the current index of the first word plus one, or if it doesn't mach the letter at the same index, 
        return count. Otherwise add the letter to count. If you get through the entire array, return count.
        """
        count = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) < i+1 or strs[j][i] != strs[0][i]:
                    return count
            count += strs[0][i]
        return count
