URL: https://leetcode.com/problems/longest-common-prefix/description/

# 14. Longest Common Prefix

### Time complexity: O(n * m) where n is the length of the list and m is the length of the shortest string in the array. Space complexity: O(1).

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 
Constraints:

	1 <= strs.length <= 200
	0 <= strs[i].length <= 200
	strs[i] consists of only lowercase English letters.

# Thoughts:
Pretty easy. Just iterate though the entire list and using the first word, see if if each letter at the index matches with all the others. If a letter doesn't match, return the amount of times you've iterated, i + 1. If you finish the loop, 
return the length of the first string plus 1. If a string is shorter than the first string and you get to it at a bigger index than it's length, stop iterating and return i + 1.
