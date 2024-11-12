# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # This is the recursive solution
        """
        if not root:
            return []
        ans = []
        def preorder(node):
            ans.append(node.val)
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
        preorder(root)
        return ans
        """
        # This is the iterative solution
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack[-1]
            stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
        
