def preorder(root):
    result=[]
    def dfs(node):
        if not node:
            return True
        result.append(node.data)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return result
