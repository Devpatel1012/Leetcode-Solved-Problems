class Solution:
    def __init__(self):
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []

    def findMode(self, root):
        
        def inorder(node):
            if not node:
                return
            
            # Left
            inorder(node.left)
            
            # Process current node
            if node.val == self.current_val:
                self.current_count += 1
            else:
                self.current_val = node.val
                self.current_count = 1
            
            # Update modes
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]
            elif self.current_count == self.max_count:
                self.modes.append(node.val)
            
            # Right
            inorder(node.right)
        
        inorder(root)
        return self.modes