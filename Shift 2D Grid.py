class Solution(object):
    def shiftGrid(self, grid, k):
        rows, cols = len(grid), len(grid[0])

        for _ in range(k):
            ans = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    if i == 0 and j == 0:
                        ans[i][j] = grid[rows - 1][cols - 1]
                    elif j == 0:
                        ans[i][j] = grid[i - 1][cols - 1]
                    else:
                        ans[i][j] = grid[i][j - 1]

            grid = ans

        return grid