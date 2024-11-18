URL: https://leetcode.com/problems/two-sum/description/

# 1. Two Sum

### Space and time complexity: O(n)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 
Constraints:

	2 <= nums.length <= 104
	-109 <= nums[i] <= 109
	-109 <= target <= 109
	Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Thoughts:
Very basic but important problem. I once struggled with this problem, then I learned what dictionaries were. Firstly, I want to say that this problem might be one of the most important to know. I've heard you must know it for interviews. 
My solution just consisted of putting in every number in the array into a dictionary with the numbers as the keys and their indices as the values. If a number was already in the dictionary, we skip it unless it's equal to half of the target 
number. After completing the dictionary, we delete dict[target/2] to lessen the operations in the future and prevent silly errors. Then we iterate through the list again and see if target - nums[i] is in the array. if it is, we return 
[i, dict[nums[i]]]. Overall one of my favorite problems. It is a must-do to solve more advanced problems like the torturous 3sum (lmao) problem.
