class Solution(object):

    def splittingNumber(self, number):
        m = number % 10
        z = number // 10
        return z, m  

    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = self.splittingNumber(total)  

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next  

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

solution = Solution()
l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linkedlist([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))  