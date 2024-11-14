# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recusive solution
        def recursion(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return recursion(node1.left, node2.right) and recursion(node1.right, node2.left)
        
        #return recursion(root.left, root.right)

        # Iterative solution
        stack1, stack2 = [root], [root]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 == None and node2 == None:
                continue
            elif node1 == None or node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            stack1.append(node1.right)
            stack1.append(node1.left)
            stack2.append(node2.left)
            stack2.append(node2.right)
        return True
