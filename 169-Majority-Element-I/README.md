URL: https://leetcode.com/problems/majority-element/description/

# 169. Majority Element

### Complexity for dictionary solution: O(n) for time and space. Complexity for Boyer-Moore algorithm: O(n) time, O(1) space.

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

 
Constraints:

	n == nums.length
	1 <= n <= 5 * 104
	-109 <= nums[i] <= 109

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

# Thoughts:
I learned a lot from this problem, mainly how the Boyer-Moore algorithm works. Basically, as you iterate through the list, you keep track of the current value and the number of it. We start with our candidate being the first element and a count of 1. When 
we get to the next element, we check if it's the same as our candidate. If it is, we add 1 to the count. If it isn't, we SUBTRACT 1. We subtract it because it's kind of like a vote canceling out another vote, if that makes sense. Then we check 
if the count of the candidate is equal to zero, we replace it with the current element. After iterating the entire list, we return the candidate. As I mentioned, this works because the votes kind of cancel each other out.
