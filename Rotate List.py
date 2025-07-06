# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # if not head or not head.next or k == 0:
        #     return head

        # for i in range(k):
        #     node = head
        #     # Traverse to the second-last node
        #     while node.next and node.next.next:
        #         node = node.next

        #     # node now points to the second-last node
        #     temp = node.next
        #     node.next = None
        #     temp.next = head
        #     head = temp

        # return head
        
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make the list circular
        tail.next = head

        # Step 3: Find the new tail position
        k = k % length  # In case k is larger than length
        steps_to_new_tail = length - k

        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the circle

        return new_head


        