class Solution(object):
    def findAllPeople(self, n, m, f):
        parent  = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            parent[find(x)] = find(y)
        
        union(0,f)
        m.sort(key = lambda x: x[2])
        i = 0

        while i<len(m):

            time = m[i][2]
            people = []

            while i<len(m) and m[i][2] == time:
                x,y,_ = m[i]
                union(x,y)
                people.append(x)
                people.append(y)
                i +=1

            for p in people:
                if find(p) != find(0):
                    parent[p] = p
        
        
        return [i for i in range(n) if find(i) == find(0)]

        