URL: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# 145. Binary Tree Postorder Traversal

### Time complexity: O(n) for both methods. Space complexity: O(h) for both, where h is the height of the tree. O(n) at the worst case.

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 
Constraints:

	The number of the nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?

# Thoughts:
I absolutely love traversing trees. For the recursive solution of this problem, we simply visit the left child until we can't, append it to our array, visit the right node until we can't, and repeat. For the iterative solution, it's the 
same logic except we use a stack to store the nodes and a set to prevent visiting previously visited nodes. If there is not a left child, check if there is a right child. If there is, append it to our stack and go back to the start of the 
while loop. After the while loop is done, we return our array. I feel giddy doing these because they are so satisfying.
