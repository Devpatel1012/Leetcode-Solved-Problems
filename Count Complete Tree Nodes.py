# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0
        
        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        
        lh, rh = leftHeight(root), rightHeight(root)
        
        if lh == rh:  # perfect tree
            return (1 << lh) - 1  # 2^h - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        # ar=[]
        # def inorder(root):
        #     if not root:
        #         return 0
        #     inorder(root.left)
        #     ar.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return len(ar)