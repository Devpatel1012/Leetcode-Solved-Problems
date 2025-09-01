# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # if not root:
        #     return False  # should return boolean
        
        # # If it's a leaf node, check if path sum matches
        # if not root.left and not root.right:
        #     return targetSum == root.val
        
        # # Recurse left and right, reducing the target sum
        # return (self.hasPathSum(root.left, targetSum - root.val) or
        #         self.hasPathSum(root.right, targetSum - root.val))
    
        if not root:return False
        def path(root,targetSum,s):
            if not root:return False
            s+=root.val
            if not root.left and not root.right:return s==targetSum
            return path(root.left,targetSum,s) or path(root.right,targetSum,s)
        return path(root,targetSum,0)
        