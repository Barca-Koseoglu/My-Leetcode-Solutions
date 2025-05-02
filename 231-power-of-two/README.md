URL: https://leetcode.com/problems/power-of-two/description/

# 231. Power of Two

### Runtime: O(1), Space: O(1)

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 
Constraints:

	-231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?

# Thoughts:
Using a module or using loops and recursion is trivial. The best way to do it is with bit manipulation. A power of two in binary always has only one bit set to 1, and that is the leftmost bit. To see if it is right, you can take the number 
and use the & operation (if two bits at the same spot are 1 then return 1, else return 0) with a number 1 less than the original. If the original number is a power of 2, then it looks like 1000..... & 999..... == 0. Else, we return False. 
We imediately return False if it's less than 1 as well.
