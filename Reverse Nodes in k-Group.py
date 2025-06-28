# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # Helper function to check if there are at least k nodes left
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        # Helper function to reverse k nodes
        def reverseKNodes(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            if not hasKNodes(kth.next, k):
                break

            # Move to the k-th node
            for i in range(k):
                kth = kth.next

            group_next = kth.next
            # Reverse k nodes
            prev, curr = None, group_prev.next
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tail = group_prev.next  # New tail after reversal
            group_prev.next = prev  # Connect previous part to reversed part
            tail.next = group_next  # Connect reversed part to remaining list

            group_prev = tail  # Move the pointer to the tail for next group

        return dummy.next
