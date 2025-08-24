# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_balance_and_height(node):
            if node is None:
                return True, 0  # (is_balanced, height)

            left_balanced, left_height = check_balance_and_height(node.left)
            right_balanced, right_height = check_balance_and_height(node.right)

            # Check if current node is balanced
            current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            # Calculate height of current node
            current_height = max(left_height, right_height) + 1

            return current_balanced, current_height

        is_balanced, _ = check_balance_and_height(root)
        return is_balanced