# No type hints needed for older Python versions
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists): # Removed type hint: lists: List[ListNode]
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Helper function to merge two sorted linked lists
        def mergeTwoLists(l1, l2): # Removed type hints: l1: ListNode, l2: ListNode -> ListNode
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1:
                current.next = l1
            elif l2:
                current.next = l2
            return dummy.next

        # Iteratively merge lists using a divide and conquer strategy
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                # Ensure we don't try to access an index out of bounds
                if i + interval < len(lists):
                    lists[i] = mergeTwoLists(lists[i], lists[i + interval])

            interval *= 2

        return lists[0] if lists else None