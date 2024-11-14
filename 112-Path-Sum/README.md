URL: https://leetcode.com/problems/path-sum/description/

# 112. Path Sum

### Time complexity: O(n). Space complexity: O(h) where h is the hieght of the tree, worst case O(n) best case O(log n)

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 
Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

 
Constraints:

	The number of nodes in the tree is in the range [0, 5000].
	-1000 <= Node.val <= 1000
	-1000 <= targetSum <= 1000

# Thoughts:
Honestly this was an annoying problem. I haven't dealt with many binary tree problems or recursion problems yet, but getting the output for this problem was tricky. At first I just tried putting all the sums up to the leaf node into a set 
then seeing if targetSum was in it, but I came to the conclusion that it was unnecesary and I could do it inside the function. I thought of using "or" to see if there was the targetSum. The logic is simple: when you get to a leaf node, 
add the value of it to total, the value thus far, and compare it with targetSum. If it's the same, return True. But I didn't know what to do with the return value after iterating, or how to see if two child nodes had a true or false value. 
After thinking about it for some time, I came to the realization that I can just do preorder traversal and set a variable to the function call inside the function. Then I would return left or right. Since it's recursive, It always works out.
