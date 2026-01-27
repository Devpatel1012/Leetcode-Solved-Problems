
class Solution(object):
    def minCost(self, n, edges):
        ed = defaultdict(set)

        for x, y, w in edges:
            ed[x].add((y,w))
            ed[y].add((x,2*w))
            
        heap = [(0,0)]
        dis = [float("inf")] * n
        seen = {0}
        dis[0] = 0

        while heap:
            current_cost, u = heapq.heappop(heap)
            
            seen.add(u)
            if u == n-1:
                return current_cost

            for v, cost in ed[u]:
                    if  dis[v] > dis[u] + cost:
                        dis[v] = dis[u] + cost
                        heapq.heappush(heap, (dis[v], v))
        
        return  -1
