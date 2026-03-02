class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)
        t = []
        for row in grid:
            cou = 0
            for val in reversed(row):
                if val == 0:
                    cou+=1
                else:
                    break
            t.append(cou)
        
        swaps = 0

        for i in range(n):
            needed = n-1-i
            j = i
            while j<n and t[j]<needed:
                j+=1
            if j == n:
                return -1
            while j>i:
                t[j],t[j-1] = t[j-1],t[j]
                swaps+=1
                j-=1
        return swaps