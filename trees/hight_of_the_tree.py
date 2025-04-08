def hight_of_tree(root):
    if root is None:
        return 0
    left=hight_of_tree(root.left)
    right=hight_of_tree(root.right)
    return 1+ max(left,right)
