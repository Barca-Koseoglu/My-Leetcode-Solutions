URL: https://leetcode.com/problems/longest-palindromic-substring/description/

# 5. Longest Palindromic Substring

### Brute force time: O(n<sup>3</sup>), Fastest solution time: O(n<sup>2</sup>), Space: O(n)

Given a string s, return the longest palindromic substring in s.

 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 
Constraints:

	1 <= s.length <= 1000
	s consist of only digits and English letters.

# Thoughts
A very fun and easy problem. The brute force of this is to go through each and every substring from the smallest to the largest using a sliding window technique and a nested loop. The substrings by default makes this problem AT LEAST 
O(n<sup>2</sup>) runtime and O(n) space complexity. Then, you can use a function that checks if it's a palindrome. The function would use two pointers and go through starting from the start and end of the word and checking if they're the 
same until the pointers cross. This is what I call inefficient brute force. It's O(n<sup>3</sup>) still, but it checks the WHOLE thing. A way to make it more efficient is to start from the largest substring and keep going. If one is a palindrome, 
then stop. That is automatically the biggest one. This is actually accepted by leetcode even though it's O(n<sup>3</sup>), although it takes like three whole seconds to run. The efficient way is pretty straightfoward, but a bit harder to 
implement. What you do is go through the list normally, and for each character you come across, use two pointers to go left and right outward one by one until either you get to the end of a side or the pointers don't have the same value. There's 
a bunch of tweaking and technical stuff about this. But this only works for odd-lengthed substrings. For even lengthed substrings, I made a WHOLE other version, this time going through the length of the list minus one, the p1 and p2 will be at 
i-1 and i+2 respectively. Then do the exact same thing. There's even more little technical bits, but the theory is simple.
