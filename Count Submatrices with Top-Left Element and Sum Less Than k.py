class Solution(object):
    def countSubmatrices(self, grid, k):
        n = len(grid)
        m = len(grid[0])

        ans = 0

        for i in range(n):
            for j in range(m):
                if i == 0  and j == 0:
                    if(grid[i][j] <= k):
                        ans+=1
                    else:
                        return 0
                
                elif i == 0 and j>0:
                    grid[i][j] += grid[i][j-1]
                    if grid[i][j] <= k:
                        ans+=1
                    else:
                        continue
                elif j == 0 and i>0:
                    grid[i][j] += grid[i-1][j]
                    if grid[i][j] <= k:
                        ans+=1
                    else:
                        continue
                else:
                    grid[i][j] += (grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1])
                    if grid[i][j] <= k:
                        ans+=1
                    else:
                        continue
        return ans

