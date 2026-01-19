class Solution(object):
    def maxSideLength(self, mat, require):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        ans = 0
        n = len(mat)
        m = len(mat[0])
        ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                ps[i+1][j+1] = ps[i+1][j] + ps[i][j+1]-ps[i][j]+mat[i][j]
        exp = 0
        for i in range(n):
            for j in range(m):
                if min(i,j)>=exp:
                    pre_sum = ps[i+1][j+1] -ps[i-exp][j+1] -ps[i+1][j-exp] + ps[i-exp][j-exp]
                    if pre_sum <= require:
                        exp += 1
        return exp
