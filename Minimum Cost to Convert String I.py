class Solution(object):
    def floydWarshall(self, adjList):
        nover = 26
        dist = [[float('inf')] * nover for _ in range(nover)]

        # distance to self = 0
        for i in range(nover):
            dist[i][i] = 0

        # initialize edges
        for i in range(nover):
            for nei in adjList[i]:
                dist[i][nei[0]] = min(dist[i][nei[0]], nei[1])

        # Floyd-Warshall
        for k in range(nover):
            for i in range(nover):
                for j in range(nover):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    def minimumCost(self, source, target, original, changed, cost):
        nover = 26
        adjList = [[] for _ in range(nover)]

        for i in range(len(cost)):
            fromChar = ord(original[i]) - ord('a')
            targetChar = ord(changed[i]) - ord('a')
            transformCost = cost[i]
            adjList[fromChar].append((targetChar, transformCost))

        dist = self.floydWarshall(adjList)
        ans = 0

        for i in range(len(source)):
            sourcechar = ord(source[i]) - ord('a')
            targetchar = ord(target[i]) - ord('a')

            if source[i] != target[i]:
                if dist[sourcechar][targetchar] == float('inf'):
                    return -1
                ans += dist[sourcechar][targetchar]

        return ans
