URL: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# 345. Reverse Vowels of a String

Time: 7 ms, Memory: 17.66 MB

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 
Constraints:

	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

# Thoughts:
This was a really simple question. I simply turned the string into a list, made a set called check of upper and lowercase vowels, and made two pointers p1 and p2 that start at 0 and len(s)-1 respectively. If p1 or p2 were not on a vowel,
then increase and decrease them by 1 respectively. When they're both in check, AKA they're both vowels, swap them and increase p1 by 1 and decrease p2 by 1. Keep doing this until p2 is smaller than or equal to p1, meaning it has gone over
p1. Then turn the list into a string and return it.
