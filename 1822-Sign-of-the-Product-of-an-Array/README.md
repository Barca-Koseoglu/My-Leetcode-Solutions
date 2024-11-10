URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=study-plan-v2&envId=programming-skills

# 1822. Sign of the Product of an Array

Time: 0 ms, Memory, 16.65 MB

Implement a function signFunc(x) that returns:

	1 if x is positive.
	-1 if x is negative.
	0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

 
Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

 
Constraints:

	1 <= nums.length <= 1000
	-100 <= nums[i] <= 100

# Thoughts:
Iterate through the list. If there is a zero, anything times 0 is 0, so return 0. If there isn't a zero, keep count of the negative numbers in the array. If there is an even number, return 1 since multiplying a negative an even amount 
of times makes it positive. Otherwise, return -1. Easiest one I've done in a while.
