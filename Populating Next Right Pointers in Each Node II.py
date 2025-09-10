"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # if not root:
        #     return None
            
            
        # current_level = [root]
                
        # while current_level:
        #     next_level = []
                    
        #             # Process all nodes at the current level
        #     for i in range(len(current_level)):
        #         node = current_level[i]
                        
        #                 # Set next pointer if not the last node in level
        #         if i < len(current_level) - 1:
        #             node.next = current_level[i + 1]
                        
        #                 # Add children to next level
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
                    
        #     current_level = next_level
        # return root
        if not root:
            return None
        
        # from collections import deque
        q = deque([root])   # start BFS
        
        while q:
            size = len(q)
            # prev = None
            for i in range(size):
                node = q.popleft()
                
                if i< size-1:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # last node in the level → next is None
            # prev.next = None
        
        return root