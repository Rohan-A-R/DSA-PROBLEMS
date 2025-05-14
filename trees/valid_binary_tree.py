def valid_binary(node):
    def helper(node,left,right):
        if not node:
            return True
        if node.val<left and node.val>right:
            return False
        helper(node.left,node.val,left)
        helper(node.right,right,node.val,)

    helper(node,float('-inf'),float('inf'))
    