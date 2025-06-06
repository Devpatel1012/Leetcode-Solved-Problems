# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Remove type hints from here
    def removeNthFromEnd(self, head, n):  # Modified line
        """
        Removes the nth node from the end of a linked list and returns its head.

        This solution uses the two-pointer approach (slow and fast pointers).
        The fast pointer is moved n+1 steps ahead of the slow pointer.
        Then, both pointers move one step at a time until the fast pointer
        reaches the end of the list. At this point, the slow pointer will
        be at the node *before* the one to be removed.

        Args:
            head: The head of the singly-linked list.
            n: The position of the node to be removed from the end.

        Returns:
            The head of the modified linked list.
        """
        dummy = ListNode(0, head)  
        slow = fast = dummy
        

        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        

        slow.next = slow.next.next
        
        return dummy.next 