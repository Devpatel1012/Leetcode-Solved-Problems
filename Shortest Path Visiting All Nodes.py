class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        if n == 1:
            return 0
        target = (1 << n) - 1      
        queue = deque()
        visited = set()
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, dist = queue.popleft()

            for nei in graph[node]:
                new_mask = mask | (1 << nei)

                if new_mask == target:
                    return dist + 1

                if (nei, new_mask) not in visited:
                    visited.add((nei, new_mask))
                    queue.append((nei, new_mask, dist + 1))
                
