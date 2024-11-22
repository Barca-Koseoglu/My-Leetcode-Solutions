URL: https://leetcode.com/problems/majority-element-ii/description/

# 229. Majority Element II

### Complexities: O(n) space and time for dictionary solutions, O(1) for space and O(1) for time for the Boyer-Moore Algorithm solution

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 
Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

 
Constraints:

	1 <= nums.length <= 5 * 104
	-109 <= nums[i] <= 109

 
Follow up: Could you solve the problem in linear time and in O(1) space?

# Thoughts:
This one was easy to find with the dictionary but stupidly annoying with the algorithm. The algorithm's logic is basically this: find the two most commonly occuring elements (max since only two can be greater than 1/3) and then find out if they 
actually are greater than 1/3. Instead of variables, though, I used a dictionary. Why? Because I generalized the problem to the k-1 most commonly occuring elements where k is a constant and the elements have to be bigger than 1/k. I stored the 
counts of numbers I iterated through in the dictionary. Whenever the length of the dicitonary exceeded two, I made a new dictionary that put in the elements of the old dictionary if their counts were greater than one, then subtrated them by 1 and replaced the old dictionary with the new one. 
After doing this, I have the most commonly occuring numbers, although it doesn't guarantee that they're both greater than a third of the list rounded down. So in order to find out if they are, I create a new array and check both dictionary 
values to see if they're counts are greater than len(nums) // 3. If they are, append them to the array and return it. Overall it was a decent question but super annoying.
