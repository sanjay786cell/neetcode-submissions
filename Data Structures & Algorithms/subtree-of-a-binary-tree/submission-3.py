# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s = root
        t = subRoot
        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s,t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(seld, s, t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return seld.sameTree(s.left, t.left) and seld.sameTree(s.right, t.right)

        return False