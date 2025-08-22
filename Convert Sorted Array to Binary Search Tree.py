# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2   # Choose middle element
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)   # Left half → left subtree
            node.right = helper(mid + 1, right) # Right half → right subtree
            return node

        return helper(0, len(nums) - 1)
        # if not nums:
        #     return None
        # mid=len(nums)//2
        # root=TreeNode(nums[mid])

        # root.left=self.sortedArrayToBST(nums[:mid])
        # root.right=self.sortedArrayToBST(nums[mid+1:])

        # return root
        