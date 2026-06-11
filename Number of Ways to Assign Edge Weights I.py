class Solution(object):
    def assignEdgeWeights(self, edges):
        MOD = 10**9+7
        n = len(edges)+1
        g = [[] for _ in range(n+1)]

        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(g,x,f):
            max_dep = 0
            for y in g[x]:
                if y == f:
                    continue
                max_dep = max(max_dep, dfs(g,y,x)+1)
            return max_dep

        max_dep = dfs(g,1,0)
        return pow(2,(max_dep-1),MOD)
        

        