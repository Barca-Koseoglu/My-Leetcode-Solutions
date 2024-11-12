URL: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# 144. Binary Tree Preorder Traversal

### Time Complexity: O(n) for both solutions. Space complexity: O(h) for both if h is the height, O(n) for the worst case.

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

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
Trees are my second favorite data structure next to hash maps. For the recursive solution of pre-order traversal, we start at the root node, add the value into our return array, then check if the left child exists **first**. If it does, we 
run recursively run the function again with node.left being our root node. After encountering a root with node.left == None, we check the right node and recursively go down that path. Once everything is finished, we exit the function and 
return our array of values. For he iterative solution, we obviously can't use a for loop so we would use a while loop. We also need a stack to store the nodes we need to visit. We start with stack = [root]. We remove the rightmost node 
and append the value to our array. We also have to put the right and left children of the node onto our stack, in that order. If the it doesn't have a child or children, don't append anything onto the stack. Once we go through all the 
values, our stack will be empty and we can leave the while loop. Then we return our list of values. I have a really strong love for these types of tree problems, since they remind me of search algorithms AI uses.
