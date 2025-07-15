from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = deque([root] if root else [])
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Reverse the level list if the current level is odd-indexed (for zigzag)
            if len(res) % 2 == 1:
                level.reverse()
            
            res.append(level)
        
        return res