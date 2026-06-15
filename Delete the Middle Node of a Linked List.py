class Solution(object):
    def deleteMiddle(self, head):
        if head.next == None:
            return None

        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        slow.next = None

        return head

        