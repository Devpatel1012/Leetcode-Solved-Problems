# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        # Hashmap for fast index lookup in inorder
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Helper function
        def build(in_left, in_right):
            if in_left > in_right:
                return None
            
            # Last element in postorder is root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Get inorder index
            idx = idx_map[root_val]
            
            # Build right subtree first (because of postorder popping)
            root.right = build(idx+1, in_right)
            root.left = build(in_left, idx-1)
            
            return root
        
        return build(0, len(inorder)-1)