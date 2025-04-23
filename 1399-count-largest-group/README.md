URL: https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23

# 1399. Count Largest Group

### Runtime: O(nlogn), Space: O(logn)

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 
Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

 
Constraints:

	1 <= n <= 104

# Thoughts:

This was a very easy problem, but what made it interesting was the runtime and space complexity. They aren't both O(n), wich surprised me at first but then I realized why they were like that. The time complexity is O(nlogn) because 1. The 
loop iterates O(n) times and 2. each number needs to be converted into a string and iterated over the digits, so the maximum number of digits for any number up to n is log10(n). Therefore, the inner loop takes O(log n) time in the worst 
case. WORST CASE, though, but for these constraints it has a very low influence. The space being O(logn) is also pretty straightforward: the maximum possible group sum for any number up to n is 9 times the number of digits in n, which is 
at most 9 * log10(n). Thus, the number of unique group sums is limited. Big O doesn't care about constants, so we smack off that nine and get O(logn) as our worst case space complexity.
