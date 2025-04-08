class Solution:
    def diameterOfBinaryTree(self, root):
        self.res=0
        def dfs(root):
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.res=max(self.res,left+right)
            return 1+max(left,right)
        dfs(root)
        return self.res