class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        
        adj = defaultdict(list)

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        res = [0]

        def dfs(curr,parent):
            total = values[curr]

            for child in adj[curr]:
                if child != parent:
                    total += dfs(child,curr)

            if total%k == 0:
                res[0] +=1

            return total
            
        dfs(0,-1)

        return res[0]

