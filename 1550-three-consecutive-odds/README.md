URL: https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11

# 1550. Three Consecutive Odds

### Runtime: O(n), Space: O(1)

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

 
Constraints:

	1 <= arr.length <= 1000
	1 <= arr[i] <= 1000

# Thoughts
Very easy problem to start the day, just iterating from 2 to the length of arr and checking whether the two spots that came right before, as well as the spot itself, is not divisible by 2 using modular division and seeing if it equals to one.
