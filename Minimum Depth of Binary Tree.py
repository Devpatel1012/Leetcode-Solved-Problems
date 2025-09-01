# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        # if no left child, recurse on right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # if no right child, recurse on left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # if both children exist, take the min depth
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        