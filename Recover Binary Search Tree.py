# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Detect violation: previous node value > current node value
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node

            inorder(node.right)

        # Step 1: Find the two swapped nodes
        inorder(root)

        # Step 2: Swap their values back
        self.first.val, self.second.val = self.second.val, self.first.val

        
        # self.temp = []
        # def inorder(node):
        #     if not node: return 
        #     inorder(node.left)
        #     self.temp.append(node)
        #     inorder(node.right)
        # inorder(root)
        # srt = sorted(n.val for n in self.temp)
        # for i in range(len(srt)):
        #     self.temp[i].val = srt[i]


