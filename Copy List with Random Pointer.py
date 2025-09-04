"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # hashmap = {}
        # node = head
        # i = 0
        # while node.next :
        #     hashmap[i] = {'val':node.val, 'next': node.next,'random': node.random}
        #     node = node.next
        #     i+=1
        # print(hashmap)
        # root = Node(hashmap[0]['val'])
        # root.next = hashmap[0]['next']
        # root.random = hashmap[0]['random']

        # for i in range(1,len(hashmap)-1):
        #     node = Node(hashmap[i]['val'])
        #     node.next = hashmap[i]['next']
        #     node.random = hashmap[i]['random']
        # return root

        # if not head:
        #     return None

        # # Step 1: Create a mapping from old nodes to new nodes
        # old_to_new = {}

        # cur = head
        # while cur:
        #     old_to_new[cur] = Node(cur.val)
        #     cur = cur.next

        # # Step 2: Assign next and random pointers
        # cur = head
        # while cur:
        #     old_to_new[cur].next = old_to_new.get(cur.next)
        #     old_to_new[cur].random = old_to_new.get(cur.random)
        #     cur = cur.next

        # # Step 3: Return head of new list
        # return old_to_new[head]

        if not head:
            return None
        
        curr = head
        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp=temp.next.next
        
        temp = head
        dummy = Node(-1)
        curr = dummy
        while temp:
            curr.next = temp.next
            temp.next = temp.next.next
            curr = curr.next
            temp = temp.next
        return dummy.next
            
        

