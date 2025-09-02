# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root,path,s):
            if not root:
                return
            s+=root.val
            path.append(root.val)
            if not root.left and not root.right and s==targetSum:
                res.append(list(path))
            dfs(root.left,path,s)
            dfs(root.right,path,s)
            path.pop()
        dfs(root,[],0)
        return res