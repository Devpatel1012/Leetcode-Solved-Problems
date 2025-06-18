# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result = []
        def MAX  (node,level):
            if node == None:
                return 0
            if node.left:
                MAX(node.left,level+1)
            if node.right:
                MAX(node.right,level+1)
            result.append(level)
        MAX(root,1)
        return(max(result))