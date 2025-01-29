# Binary Tree Node Definition
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
# Insertion in BST

def  insert(root,key):
    if root is None:
        return  TreeNode(key)
    
    if key <root.value:
        root.left=insert(root.left,key)
    elif key > root.value:
        root.right=insert(root.right,key)

    return root

def inorder_traverssel(root):
    if root:
        inorder_traverssel(root.left)
        print(root.value,end=" ")
        inorder_traverssel(root.right)

root = None
root= insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root= insert(root, 80)

# Searching
def search(root, key):
    # Base case: root is None or key is present at root
    if root is None or root.value == key:
        return root

    # Key is smaller than root's value
    if key < root.value:
        return search(root.left, key)
    
    # Key is larger than root's value
    return search(root.right, key)

# Example Usage
result = search(root, 60)
print("Found" if result else "Not Found")  # Output: Found

result = search(root, 90)
print("Found" if result else "Not Found")  # Output: Not Found

def delete(root, key):
    if root is None:
        return root

    # Traverse the tree
    if key < root.value:
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        # Node with one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the in-order successor
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Example Usage
root = delete(root, 70)
inorder_traverssel(root)


