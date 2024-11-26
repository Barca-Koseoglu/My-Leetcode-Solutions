URL: https://leetcode.com/problems/first-unique-character-in-a-string/description/

# 387. First Unique Character in a String

### Time and space complexity: O(n)

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 
Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 
Constraints:

	1 <= s.length <= 105
	s consists of only lowercase English letters.

# Thoughts:
This problem just utilizes a dictionary to store the counts of the letters, then goes through each letter and checks if its count is 1 and returns -1 if 
none of the letters appear once. I think in this version of python you can make a dictionary for the counts of objects then iterate over the dictionary 
itself since the order you insert things into the dictionary is maintained. If it is possible, I'll show the solution in the code under the first one.
