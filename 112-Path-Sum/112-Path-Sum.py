# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def path(node, total):
            total += node.val
            left, right = False, False
            if not node.left and not node.right:
                return total == targetSum
            if node.left:
                left = path(node.left, total)
            if node.right:
                right = path(node.right, total)
            return left or right
        return path(root, 0)
        
