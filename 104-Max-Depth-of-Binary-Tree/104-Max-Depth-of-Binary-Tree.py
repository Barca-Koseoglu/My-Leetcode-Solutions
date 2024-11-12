# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # top-down solution
        """
        if not root:
            return 0
        def depth(node, l, big):
            if node.left:
                big = depth(node.left, l+1, big)
            if node.right:
                big = depth(node.right, l+1, big)
            big = max(big, l)
            return big
        big = 1
        return depth(root, 1, big)
        """
        # bottom-up solution
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right))+1
        return depth(root)
