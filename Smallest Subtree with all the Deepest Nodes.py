# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(root):
            if root is None :
                return (0,None)
            
           
            llevel,lnode = dfs(root.left)
           
            rlevel,rnode = dfs(root.right)
            
            if llevel>rlevel:
                return (llevel+1,lnode)
            if rlevel>llevel:
                return (rlevel+1,rnode)
            
            return (llevel+1,root)

        return dfs(root)[1]
    


        




        