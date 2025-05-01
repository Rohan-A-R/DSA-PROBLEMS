from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are null
        if not p and not q:
            return True
        
        # If one is null and the other is not
        if not p or not q:
            return False
        
        # If values differ
        if p.val != q.val:
            return False
        
        # Recur for left and right children
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
