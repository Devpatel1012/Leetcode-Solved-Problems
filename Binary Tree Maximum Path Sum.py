# SOlution 1 : "This is my logic to solve problem but it have bery high time and space complexity"

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from typing import Optional

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         result = []

#         def MaxPath(root):
#             if not root:
#                 return 0
#             left = MaxPath(root.left)
#             right = MaxPath(root.right)
#             # return max path including current node and one subtree (used for recursion upward)
#             return max(root.val, root.val + max(left, right))

#         def MaxPathForEachNode(root):
#             if not root:
#                 return
#             currleft = MaxPath(root.left) if root.left else 0
#             currright = MaxPath(root.right) if root.right else 0

#             # Only include child paths if they are positive
#             total = root.val
#             if currleft > 0:
#                 total += currleft
#             if currright > 0:
#                 total += currright

#             result.append(total)
#             MaxPathForEachNode(root.left)
#             MaxPathForEachNode(root.right)

#         MaxPathForEachNode(root)
#         return max(result)

# Solution 2: "Real SOlution of the problem"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      
        self.all_path_sums = [float('-inf')]

        def calculate_max_gain_from_node(node):
            if not node:
                return 0
            left_gain = max(0, calculate_max_gain_from_node(node.left))
            right_gain = max(0, calculate_max_gain_from_node(node.right))

          
            path_through_current_node = node.val + left_gain + right_gain
            self.all_path_sums.append(path_through_current_node)
           
            return node.val + max(left_gain, right_gain)

        
        calculate_max_gain_from_node(root)

        return max(self.all_path_sums)
