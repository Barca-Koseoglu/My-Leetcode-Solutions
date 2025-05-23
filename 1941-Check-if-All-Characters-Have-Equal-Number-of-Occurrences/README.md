URL: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table

# 1941. Check if All Characters Have Equal Number of Occurrences

### Runtime and space: O(n)

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 
Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

 
Constraints:

	1 <= s.length <= 1000
	s consists of lowercase English letters.

# Thoughts:
Very simple problem. Take the counts of the values, set the checking variable to the first letter in s, go through the dictionary values, if they aren't the same as s, return False, and if you get through the whole thing return True. 
I saw a simpler solution (which I had the thought of but was too lazy to test out) which just took the set of the dictionary values and checked if they were equal to 1, else returned False. Faster, but mine was technically more memory efficient.
