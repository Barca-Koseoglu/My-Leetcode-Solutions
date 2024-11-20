URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# 33. Search in Rotated Sorted Array

### Time complexity: O(log n). Space complexity: O(1)

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

 
Constraints:

	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	All values of nums are unique.
	nums is an ascending array that is possibly rotated.
	-104 <= target <= 104

# Thoughts:
I utterly hate this problem. I haven't done too many things requiring binary search before, but my god this was a horrible problem. Basically, the logic works like this: normal binary search but extra conditions, and those extra conditions 
rely on the fact that the midpoint must be in one of the sorted parts of the array. If the left pointer is smaller than midpoint (which means midpoint is in a sorted half of the array), then we check if the target is in between them. If it 
is, we move the right pointer to midpoint minus one. If it isn't, we put the left pointer to midpoint + 1. The opposite goes for if the right side is sorted. We always try to be in the half that the target is in. I hated this question 
because I was thinking of first finding the pivot using binary search, then running normal binary search on the sorted points. Unfortunately, although I know I should be able to do this, I spent hours just racking my brain on how to do it. 
Overall 3/10 question it was terrible.
