# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # recursive solution:
        """
        ans = []
        def postorder(node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            ans.append(node.val)
        postorder(root)
        return ans
        """
        # Iterative solution
        stack, ans, check = [root], [], set()
        while stack:
            node = stack[-1]
            check.add(node)
            if node.left and node.left not in check:    
                stack.append(node.left)
                continue
            elif node.right and node.right not in check:    
                stack.append(node.right)
                continue
            ans.append(node.val)
            stack.pop()
        return ans
        
