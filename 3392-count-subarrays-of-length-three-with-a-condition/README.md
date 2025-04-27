URL: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27

# 3392. Count Subarrays of Length Three With a Condition

### Runtime: O(n), Space: O(1)

Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

 
Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

 
Constraints:

	3 <= nums.length <= 100
	-100 <= nums[i] <= 100

# Thoughts:

This was very easy. Simply loop throught the length of the list minus 2, then check if list[i]+list[i+2] == list[i+1]/2. It's important not to truncate divide (//) because it wants it to be exact. Then if it's True, add 1 to a counter, and 
returnt the counter.
