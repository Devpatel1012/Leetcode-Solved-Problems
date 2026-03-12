class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
            self.parent[pb] = pa
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb

    def connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def maxStability(self, n, edges, k):
        ds = DisjointSet(n)
        edges.sort(key=lambda x: (-x[3], -x[2]))  # Sort by forced and then weight
        optional_weights = []
        min_forced_weight = float('inf')
        edges_used = 0

        for u, v, w, forced in edges:
            if forced:
                if ds.connected(u, v):
                    return -1
                ds.unite(u, v)
                min_forced_weight = w
                edges_used += 1
            else:
                if not ds.connected(u, v):
                    ds.unite(u, v)
                    optional_weights.append(w)
                    edges_used += 1
                if edges_used == n - 1:
                    break

        if edges_used != n - 1:
            return -1
        if not optional_weights:
            return min_forced_weight

        p = len(optional_weights)
        if p > k:
            return min(optional_weights[p - k - 1], 2 * optional_weights[-1], min_forced_weight)
        return min(2 * optional_weights[-1], min_forced_weight)