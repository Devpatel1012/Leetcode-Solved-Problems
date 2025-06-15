# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
     
        def traversal(r):
            if r is None:
                return        
            traversal(r.left)
            result.append(r.val)
            traversal(r.right)
        traversal(root)
        return result