class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def dfs(node, path):
            if not node:
                return
            
            # Add current node to path
            path += str(node.val)
            
            # If it's a leaf node, add path to result
            if not node.left and not node.right:
                result.append(path)
                return
            
            # Otherwise, continue with left and right children
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return result
