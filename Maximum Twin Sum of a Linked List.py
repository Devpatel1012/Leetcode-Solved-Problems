# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        second_half = self.reverseList(slow)
        
        # Step 3: Calculate twin sums and find the maximum
        first_half = head
        max_sum = 0
        
        while second_half:
            current_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_sum)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum
    
    def reverseList(self, head):
        """Helper function to reverse a linked list"""
        prev = None
        current = head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev