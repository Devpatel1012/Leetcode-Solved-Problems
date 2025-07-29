class Solution(object):
    def reverseList(self, head):
        prev = None              # Initially, the reversed list is empty.
        curr = head              # Start with the head of the original list.

        while curr:              # Loop until we reach the end of the list.
            next_temp = curr.next    # Step 1: Save the next node
            curr.next = prev         # Step 2: Reverse the current node’s pointer
            prev = curr              # Step 3: Move `prev` to current node
            curr = next_temp         # Step 4: Move to next node (original list)

        return prev              # When curr becomes None, prev is the new head.
