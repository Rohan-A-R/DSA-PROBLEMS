class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.right=None
        self.left=None


def invert_tree(root):
    if not root:
        return None
    
    root.left,root.right=root.right,root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root