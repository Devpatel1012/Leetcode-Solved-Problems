class Solution(object):
    def convertBST(self, root):

        def dfs(node, add):
            if not node:
                return add

            add = dfs(node.right, add)
            add += node.val
            node.val = add
            return dfs(node.left, add)

        dfs(root, 0)
        return root