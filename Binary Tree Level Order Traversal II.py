class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        
        def dfs(node, level):
            if not node:
                return
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result[::-1]


# from collections import deque
# from typing import Optional, List
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        
#         result = []

#         if root is None:
#             return result

#         queue = deque([root])

#         while queue:
            
#             level_size = len(queue)
            
#             current_level_nodes = []

#             for _ in range(level_size):
#                 node = queue.popleft()
                
#                 current_level_nodes.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
                
#                 if node.right:
#                     queue.append(node.right)
            
#             result.append(current_level_nodes)
        
#         return result[::-1]