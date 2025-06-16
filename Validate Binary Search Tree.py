from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev_val = -float('inf')

      

        def inorder_validate(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True


            if not inorder_validate(node.left):
                return False

            
            if node.val <= self.prev_val:
                return False

           
            self.prev_val = node.val

            if not inorder_validate(node.right):
                return False

            return True

        return inorder_validate(root)