URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills

# 1502. Can Make Arithmetic Progression From Sequence

Time: 0 ms, Memory: 16.84 MB

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 
Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

 
Constraints:

	2 <= arr.length <= 1000
	-106 <= arr[i] <= 106

# Thoughts:
Very easy. Since we have to see if the sorted array has the same difference value between two consecutive numbers for all pairs of consecutive numbers, we sort the list and take the difference of the second and first elements in the array. 
Then we iterate through it not including the final value. If the value we're on plus our difference value is not equal to the next number in the array, then we return False. If we exit the loop, we return True.
