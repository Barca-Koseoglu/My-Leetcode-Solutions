URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# 94. Binary Tree Inorder Traversal

### Time complexity: O(n) for both methods. Space Complexity: O(h) for both if h is the height of the tree, O(n) is the worst case scenario.

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 
Constraints:

	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?

# Thoughts:
Recursively, we just go left before going right and append it when we can't go left any more. Iteratively, we can use a stack, similar to pre-order traversal. But now (unless you want to delete the tree), we have to use a set to see if we 
have already visited a left child. If the left child is in it, then we append the current value to the return list and go right, if there is a right child. We delete the value off the stack and take the next value in the stack. After 
exiting the while loop, we return the array of values.
