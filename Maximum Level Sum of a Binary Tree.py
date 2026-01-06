
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

  

        queue = deque([root])
        level = 1
        curr = 1
        maxsum = float('-inf')
        while queue:
            l = len(queue)
            levelsum = 0
            for i in range(l):
                node = queue.popleft()
                levelsum+=node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if levelsum>maxsum:
                maxsum = levelsum
                level = curr
            
            curr+=1
        return level