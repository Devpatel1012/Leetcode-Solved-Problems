# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        pos = 1

        # Step 1: Move prev to node before `left`
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1

        # Step 2: Reverse logic in your described way
        reverse_head = None
        reverse_tail = curr
        while pos <= right:
            next_node = curr.next
            curr.next = reverse_head
            reverse_head = curr
            curr = next_node
            pos += 1

        # Step 3: Connect parts
        prev.next = reverse_head
        reverse_tail.next = curr

        return dummy.next

        # if not head or left == right:
        #     return head  # No change if list is empty or left == right

        # dummy = ListNode(0)  # Create a dummy node before head
        # dummy.next = head
        # prev = dummy

        # # Step 1: Move prev to the node before 'left'
        # for _ in range(left - 1):
        #     prev = prev.next

        # # Step 2: Reverse the sublist from left to right
        # curr = prev.next
        # for _ in range(right - left):
        #     temp = curr.next
        #     curr.next = temp.next
        #     temp.next = prev.next
        #     prev.next = temp

        # return dummy.next
