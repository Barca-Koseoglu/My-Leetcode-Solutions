URL: https://leetcode.com/problems/minimum-positive-sum-subarray/description/

# 3364. Minimum Positive Sum Subarray 

### Time complexity: O(n<sup>2</sup>). Space complexity: O(1)

You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray. If no such subarray exists, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

 
Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

	[3, -2] with a sum of 1
	[1, 4] with a sum of 5
	[3, -2, 1] with a sum of 2
	[-2, 1, 4] with a sum of 3

Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 
Constraints:

	1 <= nums.length <= 100
	1 <= l <= r <= nums.length
	-1000 <= nums[i] <= 1000

# Thoughts:
This problem's constraints are pretty restricted, so it's easier to use a less time efficient solution. That's why I iterated over each subarray using a nested for loop and when the index of the first for loop minus the index of the 
second for loop plus one is between l and r, then check the subarray sums. As you're going through each index, by the way, keep a variable to track the sum of them. So when you check if the sums are smaller you would see if that variable is 
smaller than the smallest, which is by default set to infinity. After going through everything, return the answer if it isn't infinity, else return -1.
