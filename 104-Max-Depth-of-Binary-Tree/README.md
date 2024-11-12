URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# 104. Maximum Depth of Binary Tree

### Time complexity: O(n) for both ways. Space complexity: O(h) for both where h is the height of the tree, O(n) is the worst case.

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 
Constraints:

	The number of nodes in the tree is in the range [0, 104].
	-100 <= Node.val <= 100

# Thoughts:
Great problem with two fundamental ways of using recursion. Top-down adds 1 at each level and traverses all the levels starting from the root, while bottom up takes the max number of it's children (0 if it is None) and adds one to it. Overall 
very easy but very important to know.
