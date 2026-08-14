import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

pq = [1]
visited[1] = True

while pq:
    u = heapq.heappop(pq)

    print(u, end=" ")

    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            heapq.heappush(pq, v)

print()