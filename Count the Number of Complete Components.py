class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        component_freq = defaultdict(int)

        for vertex in range(n):
            graph[vertex] = [vertex]

        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        for vertex in range(n):
            neighbours = tuple(sorted(graph[vertex]))
            component_freq[neighbours] += 1 
        
        return sum(1 
        for neg,fre in component_freq.items()
        if len(neg) == fre)