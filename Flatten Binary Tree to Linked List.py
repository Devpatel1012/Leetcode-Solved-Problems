# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # result = []

        # # Step 1: Preorder traversal and store values
        # def preorder_traversal(node):
        #     if not node:
        #         return
        #     result.append(node.val)              # Visit root
        #     preorder_traversal(node.left)        # Left subtree
        #     preorder_traversal(node.right)       # Right subtree

        # preorder_traversal(root)

        # # Step 2: Rebuild tree in linked-list form
        # if not result:
        #     return None  # Empty tree case

        # root.val = result[0]
        # root.left = None
        # curr = root

        # for i in range(1, len(result)):
        #     node = TreeNode(result[i]) 
        #     curr.right = node
        #     curr = node
        def helper(root):
            if not root:
                return 
            left = helper(root.left)
            right = helper(root.right)
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            return right or left or root
       
        helper(root)