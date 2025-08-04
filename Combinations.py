class Solution(object):
    def combine(self, n, k):
        result = []

        def backtrack(start, curr):
            if len(curr) == k:
                result.append(curr[:])  # add a copy
                return
            
            # Prune the loop: stop early if not enough numbers are left
            # key condition n - (k - len(curr)) + 2
            for i in range(start, n - (k - len(curr)) + 2):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(1, [])
        return result
# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         result = []
#         curr = []
#         def backtrack(start):
#             if len(curr) == k:
#                 result.append(list(curr))
#                 return
#             for i in range(start,n+1):
#                 curr.append(i)
#                 backtrack(i+1)
#                 curr.pop()
#         backtrack(1)
#         return result