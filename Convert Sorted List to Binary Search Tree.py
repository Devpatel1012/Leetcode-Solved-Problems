# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2   # Choose middle element
            node = TreeNode(arr[mid])
            node.left = helper(left, mid - 1)   # Left half → left subtree
            node.right = helper(mid + 1, right) # Right half → right subtree
            return node

        return helper(0, len(arr) - 1)
        # length = 0
        # temp = head
        # while temp:
        #     length += 1
        #     temp = temp.next

        # # Step 2: helper to get value at a given index
        # def getValueAtIndex(index):
        #     node = head
        #     for _ in range(index):
        #         node = node.next
        #     return node.val

        # # Step 3: recursive tree builder
        # def buildTree(left, right):
        #     if left > right:
        #         return None

        #     mid = (left + right) // 2
        #     # get middle value
        #     val = getValueAtIndex(mid)
        #     root = TreeNode(val)

        #     # recursively build left and right subtrees
        #     root.left = buildTree(left, mid - 1)
        #     root.right = buildTree(mid + 1, right)

        #     return root

        # return buildTree(0, length - 1)x