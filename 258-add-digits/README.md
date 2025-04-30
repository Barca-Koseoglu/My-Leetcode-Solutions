URL: https://leetcode.com/problems/add-digits/description/

# 258. Add Digits

### Runtime: O(1), Space: O(1)

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

 
Constraints:

	0 <= num <= 231 - 1

 
Follow up: Could you do it without any loop/recursion in O(1) runtime?

# Thoughts:
The recursive and iterative solutions are trivial. The mathy concept behind taking mod 9 of the number is a bit weird but cool. Every base 10 number goes like this: d<sub>1</sub> * 10<sup>0</sup> + d<sub>2</sub> * 10<sup>1</sup>... .
So, if we want to take mod 9 of that, we can actually just get rid of the 10's since mod 9 of 10 to the power of anything will always be one. That makes it CONGRUENT. So let's take the number 476. Because we want to take the mod 9 of this 
number, the decomposition is erased of powers of 10. That means it will literally just be 4 + 7 + 6 mod 9. So 17 mod 9. We can break this up into it's base 10 decomposition, and in doing so take away those powers of ten, and get 1 + 7 mod 9. 
that's 8 mod 9. So, we get the number 8 as out return value. Number theory get's you very far in computer science. Also, ust to clarify the edge cases: if we start with 0, the answer's obviosuly gonna be 0, but if the sum is a multiple of 9, 
mod 9 will return 0, so unless the starting number is 0, we return 9 if int mod 9 is 0.
