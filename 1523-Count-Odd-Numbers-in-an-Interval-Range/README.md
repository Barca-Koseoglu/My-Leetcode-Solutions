URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=study-plan-v2&envId=programming-skills

# 1523. Count Odd Numbers in an Interval Range

### O(1) time complexity

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 
Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

 
Constraints:

	0 <= low <= high <= 10^9

# Thoughts:
This was more of a math problem than a programming problem. In my head I solved it really quickly but it's really difficult for me to actually articulate my thoughts, so I'll try my best. I first thought just dividing the difference of low 
and high by two would give me the answer, but unintuitively, this is wrong. The next thing I thought about is what subtracting does. Subtraction figures out the steps to take to get from point a to b. So 8 and 2 are 6 steps away from each 
other. But what I realized is that we don't really care about b. b is only the starting point, so it counts as zero steps. This also means for addition we wouldn't care about point a since we start at it. If someone tells you to count to 5, 
you would start at 1 and go till five. But you actually start at 0; we just don't acknowldge it. So subtracting low from high doesn't include high as a step, so it doesn't acknowledge it. That's why we gotta increase high by 1. Then we can 
divide the rand of values by two. high and low still matter, though. If high and low are both initially odd, high would be even and we would need to include low in the count of even and odd, so (high - low)/2. Honestly, I can't explain it.
