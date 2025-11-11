class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(m+1)]

        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for i in range(m, zeros-1, -1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones]+1)

        return dp[m][n]