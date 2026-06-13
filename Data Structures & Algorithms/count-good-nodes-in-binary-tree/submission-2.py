# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_val=-float('inf')) -> int:
        if root is None:
            return 0
        
        gn = 0
        if root.val >= max_val:
            gn = 1
            max_val = root.val
        
        return gn + self.goodNodes(root.left, max_val) + self.goodNodes(root.right, max_val)