class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        rows = len(grid)
        cols = len(grid[0])

        if x < 0 or y < 0 or x + k > rows or y + k > cols:
            return grid

        for i in range(x, x + k // 2):
            for j in range(y, y + k):
                grid[i][j], grid[x + k - 1 - (i - x)][j] = grid[x + k - 1 - (i - x)][j], grid[i][j]

        return grid

        # l = x
        # r = x+k-1

        # while l <= r:
        #     grid[l][y:y+k], grid[r][y:y+k] = grid[r][y:y+k], grid[l][y:y+k]
        #     l += 1
        #     r -= 1
        
        # return grid