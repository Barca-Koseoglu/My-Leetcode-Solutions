from collections import deque # I only used .popleft() and .append(), no other operations since i consider that cheating

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # edge case
            return []
        dq = deque([root])
        ans = []
        while dq:
            store, add = [], []
            while dq: # second loop to put all the values in a level into one list, called add
                node = dq.popleft()
                add.append(node.val)
                if node.left:
                    store.append(node.left)
                if node.right:
                    store.append(node.right)
            dq = deque(store) # store is essential to replenish dq's values
            if add:
                ans.append(add)
        return ans
        
