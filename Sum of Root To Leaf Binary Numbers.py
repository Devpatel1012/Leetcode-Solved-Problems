class Solution(object):
    def sumRootToLeaf(self, root):

        def dfs(node, curr):
            if not node:
                return 0
            
            curr = curr*2 + node.val

            if not node.left and not node.right:
                return curr
            
            
            left=dfs(node.left, curr)
            right =dfs(node.right, curr)
                
            return left +right
            
        return dfs(root,0)
        