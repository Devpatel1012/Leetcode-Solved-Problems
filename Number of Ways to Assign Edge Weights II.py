import math

class LCA(object):
    def __init__(self, edges, root):
        self.n = len(edges) + 1
        self.m = int(math.log(self.n, 2)) + 2
        self.e = [[] for _ in xrange(self.n + 1)]
        self.d = [0] * (self.n + 1)
        self.f = [[0] * self.m for _ in xrange(self.n + 1)]

        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)

        self.dfs(root, 0)

        for i in xrange(1, self.m):
            for x in xrange(1, self.n + 1):
                self.f[x][i] = self.f[self.f[x][i - 1]][i - 1]

    def dfs(self, x, fa):
        self.f[x][0] = fa
        for y in self.e[x]:
            if y == fa:
                continue
            self.d[y] = self.d[x] + 1
            self.dfs(y, x)

    def lca(self, x, y):
        if self.d[x] > self.d[y]:
            x, y = y, x

        # Raise y to the same depth as x
        diff = self.d[y] - self.d[x]
        for i in xrange(self.m - 1, -1, -1):
            if diff & (1 << i):
                y = self.f[y][i]

        if x == y:
            return x

        for i in xrange(self.m - 1, -1, -1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]

        return self.f[x][0]

    def dis(self, x, y):
        return self.d[x] + self.d[y] - self.d[self.lca(x, y)] * 2


MOD = 1000000007
N = 100010
p2 = [0] * N


def init():
    p2[0] = 1
    for i in xrange(1, N):
        p2[i] = (p2[i - 1] * 2) % MOD


init()


class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        lca = LCA(edges, 1)
        m = len(queries)
        res = [0] * m

        for i in xrange(m):
            x, y = queries[i][0], queries[i][1]
            if x != y:
                res[i] = p2[lca.dis(x, y) - 1]

        return res