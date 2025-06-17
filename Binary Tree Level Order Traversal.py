from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs_with_level(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

           
            if level == len(result):
                result.append([]) 
            result[level].append(node.val)

            
            dfs_with_level(node.left, level + 1)
            dfs_with_level(node.right, level + 1)

        if root:
            dfs_with_level(root, 0)

        return result
    

# Second way to solve the problem
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs_with_level(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

           
            if level == len(result):
                result.append([]) 
            result[level].append(node.val)

            
            dfs_with_level(node.left, level + 1)
            dfs_with_level(node.right, level + 1)

        if root:
            dfs_with_level(root, 0)

        return result