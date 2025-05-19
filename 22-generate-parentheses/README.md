URL: https://leetcode.com/problems/generate-parentheses/description/

# 22. Generate Parentheses

### Runtme: O(2<sup>n</sup>), Space: O(2<sup>n</sup>)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

	1 <= n <= 8

# Thoughts:
I tried something new today. I wrote out what I was thinking above the actual solution and then solved it. I kind of made the stupid mistake of using @cache but other than that my entire approach was to have a number to see if 
a parentheses was valid and used recursion to add on more and more parentheses.
