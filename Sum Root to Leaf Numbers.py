# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        def dfs(root,curr):
            if not root:
                return
            curr += str(root.val)

            # If it's a leaf, save the number
            if not root.left and not root.right:
                res.append(curr)
                return

            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root,"")
        total_sum = 0
        for num_str in res:
            total_sum += int(num_str)
        return total_sum
