
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        

        MOD = 10**9+7
        sumpernode = []

        def getsum(node):
            if not node:
                return 0
            
            curr = node.val + getsum(node.left)+getsum(node.right)
            sumpernode.append(curr)
            return curr
        
        totalsum = getsum(root)
        ans = float('-inf')
        for i in sumpernode:
            ans = max(ans,(totalsum-i)*i)
        
        return ans%MOD


#  def summ(node):
       #     s = 0
        #     q = deque()
        #     q.append(node)
        #     while q :
        #         p = q.popleft()
        #         s= s+int(p.val)
        #         if p.left is not  None:
        #             q.append(p.left)
        #         if p.right is not None:
        #             q.append(p.right)
        #     return s
        
        # totalsum = summ(root)
        # MOD = 10**9+7
        # ans = float('-inf')
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     p = queue.popleft()
        #     nodesum = summ(p)
        #     ans = max(ans,(totalsum-nodesum)*nodesum)
        #     if p.left : queue.append(p.left)
        #     if p.right : queue.append(p.right)
        # return ans%MOD