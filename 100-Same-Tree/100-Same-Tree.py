# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use recursive approach
        def recursion(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return recursion(p.left, q.left) and recursion(p.right, q.right)

        # use iterative approach
        def iterative(p, q):
            stack1, stack2 = [p], [q]

            while stack1 and stack2:
                one = stack1.pop()
                two = stack2.pop()

                if one == None and two == None:
                    continue
                if one == None or two == None:
                    return False
                if one.val != two.val:
                    return False
                
                stack1.append(one.right)
                stack1.append(one.left)

                stack2.append(two.right)
                stack2.append(two.left)

            return True
        
        return recursion(p, q)
