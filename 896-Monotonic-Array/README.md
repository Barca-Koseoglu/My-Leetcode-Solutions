URL: https://leetcode.com/problems/monotonic-array/description/?envType=study-plan-v2&envId=programming-skills

# 896. Monotonic Array

Time: 36 ms, Memory: 28.24 MB

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 
Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false

 
Constraints:

	1 <= nums.length <= 105
	-105 <= nums[i] <= 105

 # Thoughts;
 Easy albeit a little annoying. We just had to find the first positive or negative difference in the array then see if all the consecutive differences have the same sign. So if the array always increases or decreases. We do not care for 
 consecutive duplicate numbers. Another tactic to solve this I just realized would be to just take away all duplicates then do it, but that would cause a mild headache for me so I'm not doing it. Anyways, we go through a while loop to find 
 the first difference in the array then go through a for loop to check if it stands. If all values are the same or the length of the array is less than 3, we return True. If a sign isn't the same, we return False. If we exit the for loop, 
 we return True.
