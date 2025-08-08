# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = head
#         while curr:
#             if curr.next and curr.val == curr.next.val:
#                 temp = curr
#                 while curr.next and curr.val == curr.next.val:
#                     curr = curr.next
#                 temp.next = curr.next
#             else:
#                 curr = curr.next
#         return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate node
                curr.next = curr.next.next
            else:
                # Move forward only when values are different
                curr = curr.next
        return head
