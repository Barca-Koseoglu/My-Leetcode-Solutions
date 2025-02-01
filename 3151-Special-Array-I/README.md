URL: https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01

# 3151. Special Array I

## Time complexity: O(n). Space complexity: O(1)

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 
Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

 
Constraints:

	1 <= nums.length <= 100
	1 <= nums[i] <= 100

# Thoughts:
This was an extremely simple problem. Basically, the key to this is using the modulo operator. Loop through all elements from 1 to len(nums) and check if that number modulus two is equal to the previous number modulus two. This works because the modulo operator takes the remainder after dividing, and the remainder after dividing by two of a number gives you 0 and 1, or even and odd respectively.
