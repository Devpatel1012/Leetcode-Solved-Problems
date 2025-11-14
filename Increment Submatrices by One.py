class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        mat = [[0]* n for _ in range(n)]
        diff = [[0]* (n+1) for _ in range(n+1)]

        for r1,c1,r2,c2 in queries:
                diff[r1][c1] += 1
                diff[r2+1][c1] -= 1
                diff[r1][c2+1] -= 1
                diff[r2+1][c2+1] += 1

        for i in range(n):
            for j in range(n):
                diff[i][j] += (diff[i-1][j] if i>0 else 0 )+(diff[i][j-1] if j>0 else 0)-(diff[i-1][j-1]if i>0 and j>0 else 0)
                mat[i][j] = diff[i][j]

        return mat