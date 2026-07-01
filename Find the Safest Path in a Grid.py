from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # -------------------------------
        # Step 1: Multi-source BFS
        # -------------------------------
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Put all thieves into the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Compute distance to nearest thief
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # -------------------------------
        # Step 2: Modified Dijkstra
        # -------------------------------

        # If start or end has a thief, answer is 0
        if dist[0][0] == 0 or dist[n-1][n-1] == 0:
            return 0

        # best[i][j] = best minimum safeness reaching (i,j)
        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        # Max heap (negative because heapq is a min heap)
        heap = [(-dist[0][0], 0, 0)]

        while heap:
            currSafe, x, y = heapq.heappop(heap)
            currSafe = -currSafe

            # Reached destination
            if x == n - 1 and y == n - 1:
                return currSafe

            # Ignore outdated entries
            if currSafe < best[x][y]:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:

                    # Minimum safeness along this path
                    newSafe = min(currSafe, dist[nx][ny])

                    if newSafe > best[nx][ny]:
                        best[nx][ny] = newSafe
                        heapq.heappush(heap, (-newSafe, nx, ny))