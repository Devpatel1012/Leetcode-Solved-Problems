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
#         node_counts = {}
#         current1 = head

#         while current1 is not None:
#             data = current1.val
#             node_counts[data] = node_counts.get(data, 0) + 1
#             current1 = current1.next
#         keys_to_remove = [key for key, value in node_counts.items() if value < 2]
#         for key in keys_to_remove:
#             node_counts.pop(key)
        
#         curr = head
#         prev = None

#         while curr:
#             # Check if the node's data is in the dictionary's keys
#             if curr.val in node_counts:
#                 if prev:
#                     prev.next = curr.next
#                 else:  # current is the head
#                     head = curr.next
#                 # No explicit deallocation needed in Python due to garbage collection
#                 curr = curr.next # Move to the next node after deletion
#             else:
#                 prev = curr
#                 curr = curr.next
#         return head
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
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check for start of duplicates
            if current.next and current.val == current.next.val:
                # Skip all duplicates
                while current.next and current.val == current.next.val:
                    current = current.next
                # Connect prev to the node after duplicates
                prev.next = current.next
            else:
                # No duplicate, move prev forward
                prev = prev.next
            current = current.next

        return dummy.next
