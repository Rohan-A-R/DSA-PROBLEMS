class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if root:
        print(root.val, end=" ")  # Process the root
        preorder(root.left)       # Recur on left subtree
        preorder(root.right)      # Recur on right subtree

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")



root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print("Preorder Traversal: ")
preorder(root) 
inorder(root) 
postorder(root)