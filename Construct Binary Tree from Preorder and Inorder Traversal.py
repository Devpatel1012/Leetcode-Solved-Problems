# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build_recursive(
            preorder_start: int, preorder_end: int,
            inorder_start: int, inorder_end: int
        ) -> Optional[TreeNode]:

            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
            root_val = preorder[preorder_start]
            root_node = TreeNode(root_val)

            root_in_inorder_idx = inorder_map[root_val]


            left_subtree_size = root_in_inorder_idx - inorder_start

            root_node.left = build_recursive(
                preorder_start + 1,                 
                preorder_start + left_subtree_size, 
                inorder_start,                     
                root_in_inorder_idx - 1             
            )

            root_node.right = build_recursive(
                preorder_start + left_subtree_size + 1,
                preorder_end,                           
                root_in_inorder_idx + 1,              
                inorder_end                            
            )

            return root_node
        return build_recursive(0, len(preorder) - 1, 0, len(inorder) - 1)


# This is second solution but the time and space complexity is higher in this

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build_recursive(
            preorder_start: int, preorder_end: int,
            inorder_start: int, inorder_end: int
        ) -> Optional[TreeNode]:

            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
            root_val = preorder[preorder_start]
            root_node = TreeNode(root_val)

            root_in_inorder_idx = inorder_map[root_val]


            left_subtree_size = root_in_inorder_idx - inorder_start

            root_node.left = build_recursive(
                preorder_start + 1,                 
                preorder_start + left_subtree_size, 
                inorder_start,                     
                root_in_inorder_idx - 1             
            )

            root_node.right = build_recursive(
                preorder_start + left_subtree_size + 1,
                preorder_end,                           
                root_in_inorder_idx + 1,              
                inorder_end                            
            )

            return root_node
        return build_recursive(0, len(preorder) - 1, 0, len(inorder) - 1)
