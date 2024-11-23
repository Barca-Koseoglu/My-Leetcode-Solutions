URL: https://leetcode.com/problems/same-tree/description/

#100. Same Tree

### Time complexity: O(n) for iterative and recursive. Space complexity: O(h) where h is the height of the tree for both iterative and recursive. Recursive is due to stack call, and iterative is due to the stack.

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 
Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

 
Constraints:

	The number of nodes in both trees is in the range [0, 100].
	-104 <= Node.val <= 104

# Thoughts:
Using preorder, iteratate through both lists simultaneously with boththe recursive and iterative methods. Set up some if statements for them to return False if two values aren't matching or one of the is None, and you got your answer. Very easy question.
