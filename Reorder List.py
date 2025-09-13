# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # Step 1: put nodes in a list
        nodeList = []
        curr = head
        while curr:
            nodeList.append(curr)
            curr = curr.next

        # Step 2: reorder nodes (head, tail, 2nd, 2nd last, ...)
        reordered = []
        left, right = 0, len(nodeList) - 1
        while left <= right:
            if left == right:
                reordered.append(nodeList[left])
            else:
                reordered.append(nodeList[left])
                reordered.append(nodeList[right])
            left += 1
            right -= 1

        # Step 3: relink nodes
        for i in range(len(reordered) - 1):
            reordered[i].next = reordered[i + 1]
        reordered[-1].next = None

        return head