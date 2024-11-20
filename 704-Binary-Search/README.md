URL: https://leetcode.com/problems/binary-search/description/

# 704. Binary Search

### Time complexity: O(n). Space complexity: O(1)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 
Constraints:

	1 <= nums.length <= 104
	-104 < nums[i], target < 104
	All the integers in nums are unique.
	nums is sorted in ascending order.

# Thoughts:
This is an extremely basic and fundamental concept. We use two pointers at the start and end of the array, then take their midpoint. If the midpoint isn't the target value, then set the right or left values to the midpoint minus or plus
one (otherwise there will be an infinite loop when the pointers are next to each other) larger or smaller than the midpoint respectively. Keep doing this while the right pointer is bigger than or equal to the left pointer. 
