# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # new sorted list head
        curr = head

        while curr:
            # At each step, insert curr into the sorted list
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_temp = curr.next  # save next node
            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            # Move to next node
            curr = next_temp

        return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def insertionSortList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not head or not head.next:
#             return head

#         curr = head
#         pos = head.next

#         while curr and pos:
#             temp = head

#             # Find first node where value is greater than pos.val
#             while temp != pos and temp.val < pos.val:
#                 temp = temp.next

#             # If insertion needed
#             if temp != pos:
#                 v1 = temp.val
#                 temp.val = pos.val
#                 temp = temp.next
#                 # Shift values until we reach pos
#                 while temp != pos:
#                     temp.val, v1 = v1, temp.val
#                     temp = temp.next
#                 temp.val = v1  # final placement
#             curr = pos
#             pos = pos.next

#         return head
