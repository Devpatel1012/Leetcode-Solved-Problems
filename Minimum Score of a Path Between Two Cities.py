class Solution(object):
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        visited = [False] * (n + 1)

        stack = [1]

        visited[1] = True

        answer = float('inf')

        while stack:

            city = stack.pop()

            for near, dist in graph[city]:

                if dist < answer:
                    answer = dist

                if not visited[near]:

                    visited[near] = True
                    stack.append(near)

        return answer