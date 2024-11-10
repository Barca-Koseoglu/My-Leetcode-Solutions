URL: https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked

# 42. Trapping Rain Water

Time: 11 ms, Memory: 18.42 MB

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 
Constraints:

	n == height.length
	1 <= n <= 2 * 104
	0 <= height[i] <= 105

# Thoughts:
This is one of my favorite two-pointer questions of all time. It sounds really tricky but in reality is very simple. What we need to do is calculate the amount of water that one column can hold in between two other columns. To do this, we need 
to know the maximum amount of water a single part of the array can hold based on the columns around it, and we have to do this for every column. So we have two pointers, p1 and p2, that start at 0 and len(list)-1 respectively. We move them 
inward (p1 += 1, p2 -= 1) until they are both bigger than zero, since that would be the start of the walls that hold the water. After this we define a value called top. Top is the smaller of p1 and p2. Also, move whichever value is smaller one 
inward. Now we can actually see how much water is contained in these values. Top is the maximum amount of water that can be filled without overfilling. Now comes the real meat of the program. A for loop runs until 
