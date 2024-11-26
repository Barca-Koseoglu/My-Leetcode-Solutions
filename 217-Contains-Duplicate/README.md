URL: https://leetcode.com/problems/contains-duplicate/description/

# 217. Contains Duplicate

### Time and space complexity: O(n)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 
Constraints:

	1 <= nums.length <= 105
	-109 <= nums[i] <= 109

# Thoughts:
This problem is fundamental to know if you ever want to work with hashes. My first solution uses a hash set and iterates over every element in nums until
it either finds a duplicate in the set, which it returns true, and if it goes through the entire list then it returns false. My second solution used the 
fact that sets can't have duplicates, so if you compare the length of the original list with the length of the list converted to a set using set(nums1), 
if they aren't equal, then it means there was at least 1 duplicate in the set.
