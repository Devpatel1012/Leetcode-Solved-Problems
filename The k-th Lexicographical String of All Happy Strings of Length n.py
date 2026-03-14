class Solution(object):
    def getHappyString(self, n, k):
        strs = []

        def backtrack(curr):
            if len(strs) == k:
                return
            if len(curr) == n:
                strs.append(curr)
                return
            
            for i in ['a','b','c']:
                if ((not curr) or (curr[-1] != i)):
                    backtrack(curr+i)
                    
        backtrack("")
        return strs[k-1] if (k <= (len(strs))) else ""

        