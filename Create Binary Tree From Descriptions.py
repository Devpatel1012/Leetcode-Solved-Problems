class Solution(object):
    def createBinaryTree(self, desc):
        tree = {}
        children = set()

        for parent, child, isLeft in desc:

            if parent not in tree:
                tree[parent] = TreeNode(parent)

            if child not in tree:
                tree[child] = TreeNode(child)

            parent_node = tree[parent]
            child_node = tree[child]

            children.add(child)

            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        for val in tree:
            if val not in children:
                return tree[val]