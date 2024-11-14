URL: https://leetcode.com/problems/symmetric-tree/description/

# 101. Symmetric Tree

### Time complexity: O(n) for both solutions. Space complexity: O(h) where h is the height of the tree, O(n) worst case for both.

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 
Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	-100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?

# Thoughts:
Recursion was pretty simple, since it's just a bunch of if statements checking if two nodes are the same. The logic for both methods is the same: use preorder traversal, but do it in opposite ways, and while you're doing that check if the 
values of the nodes match. One thing you gotta be careful about is the nodes leading to nothing. That's the biggest reason for the if statements; to check for when the nodes are none. If you don't check for empty nodes you could 
accidentally mistake an empty node with a matching node, since you skip the empty node. For the iterative solution, we would use two lists and using preorder traversal, insert the values into the list in the opposite way. But instead of 
skipping empty nodes, we put them into the lists and use if statements to check, since we would get errors otherwise. Overall, a really great problem. Recursion is something that forces you to think a good distance into the future, but that's 
what makes it so effective. 10/10 problem.
