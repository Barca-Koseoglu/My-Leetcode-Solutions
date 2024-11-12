# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive solution:
        """
        if not root:
            return []
        ans = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            ans.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans
        """
        # Iterative solution, without deleting nodes:
        if not root:
            return []
        stack, ans, check = [root], [], set()
        while stack:
            node = stack[-1]
            check.add(node)
            if node.left and node.left not in check:
                stack.append(node.left)
                continue
            ans.append(node.val)
            stack.pop()
            if node.right:
                stack.append(node.right)
        return ans
        
