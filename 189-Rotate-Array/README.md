URL: https://leetcode.com/problems/rotate-array/description/

# 189. Rotate Array

### Time complexity: O(n). Space complexity: O(1).

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 
Constraints:

	1 <= nums.length <= 105
	-231 <= nums[i] <= 231 - 1
	0 <= k <= 105

 
Follow up:

	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
	Could you do it in-place with O(1) extra space?

# Thoughts:
When I first looked at this problem, I immediately thought of using string slicing to solve the problem. This was a solution. But, according to the data on Leetcode, my solution was extraordinarily slow. At first I didn't pay any mind to 
this, but then I got to thinking: what could be an even more efficient solution? Another solution would be to literally move each element k%len(nums) steps, but that's also ineficient. After looking at the hints, I understood it. 
Reversing the list and parts of the list was the trick. Firstly, we reverse the entire list. Then, we reverse specifically num[:k]. This would be the part of that list that got rotated. Then, we return the rest of the list back to normal
by reversing nums[:k]. It's kind of a weird solution, but it is the most efficient.
