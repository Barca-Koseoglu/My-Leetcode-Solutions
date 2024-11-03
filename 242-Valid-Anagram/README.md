URL: https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

# 242. Valid Anagram

Time: 15 ms, Memory: 16.60 MB

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
Constraints:

	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Thoughts:
Very easy question. Just take the two strings, convert them into dictionaries, then see if they're equal. Also if they aren't the same length, return False. You could import counter, but I prefer not to import anything except math and 
random. 
