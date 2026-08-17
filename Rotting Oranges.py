from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        n, m = len(grid), len(grid[0])
        queue = deque()
        oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    oranges += 1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0

        def changes(row, col):
            count = 0

            for direction in directions:
                nr = row + direction[0]
                nc = col + direction[1]

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append([nr, nc])
                    count += 1

            return count

        while queue and oranges > 0:

            current_size = len(queue)

            for i in range(current_size):
                cur = queue.popleft()

                oranges -= changes(cur[0], cur[1])

            ans += 1

        if oranges > 0:
            return -1

        return ans