# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        # Step 1: Convert to list
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Step 2: Sort
        arr.sort()
        
        # Step 3: Rebuild Linked List
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next