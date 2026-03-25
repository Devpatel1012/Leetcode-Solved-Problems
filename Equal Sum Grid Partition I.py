class Solution(object):
    def canPartitionGrid(self, grid):
        n, m = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(n)) for j in range(m)]

        # Check row partition
        total = sum(rows)
        curr = 0
        for i in range(n):
            curr += rows[i]
            if curr == total - curr:
                return True

        # Check column partition
        total = sum(cols)
        curr = 0
        for j in range(m):
            curr += cols[j]
            if curr == total - curr:
                return True

        return False