class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        rows, cols = len(grid),len(grid[0])
        mod  = 10**9+7
        cache = [[[0]*k for j in range(cols+1)]for i in range(rows+1)]

        target_remain = (k - (grid[rows-1][cols-1]%k))%k
        cache[rows-1][cols-1][target_remain] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if r == rows-1 and c == cols-1:
                    continue
                for remain in range(k):
                    new_remain = (remain + grid[r][c])%k
                    cache[r][c][remain] = (
                        cache[r+1][c][new_remain]%mod +
                        cache[r][c+1][new_remain]%mod
                    )%mod
        return cache[0][0][0]

        # def dfs(r,c,remain):
        #     if r == rows-1 and c == cols-1:
        #         remain = (remain+grid[r][c])%k
        #         return 0 if remain else 1
        #     if r == rows or c == cols:
        #         return 0
        #     if cache[r][c][remain] >-1:
        #         return cache[r][c][remain]
        #     cache[r][c][remain] = (
        #         dfs(r+1,c,(remain+grid[r][c])%k)%mod +
        #         dfs(r,c+1,(remain+grid[r][c])%k)%mod 
        #     )%mod
        #     return cache[r][c][remain]
        # return dfs(0,0,0)