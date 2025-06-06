URL: https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=array

# 268. Missing Number

### Runtime: O(n), Space: O(1)

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 
Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 

 

 

 

 
Constraints:

	n == nums.length
	1 <= n <= 104
	0 <= nums[i] <= n
	All the numbers of nums are unique.

 
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Thoughts:
This was very easy, especially if you know what the sum of number from x to y will be using a formula, the sum formula. The logic behind it is that the sum of the entire range of number minus the sum of the number in the list will reveal 
the missing number, even if it's zero. Because there's only 1 missing number, adding that missing number to the sum of the list would make it equal to the sum of the whole range. Taking that equation and rearanging it, we get range_sum 
- list_sum = missing_number.
