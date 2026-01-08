class Solution(object):
    def maxDotProduct(self, num1, num2):
        n, m = len(num1), len(num2)
        NEG = -10**18
        dp = [[NEG]*m for _ in range(n)]

        dp[0][0] = num1[0] * num2[0]

        for j in range(1, m):
            dp[0][j] = max(
                num1[0] * num2[j],
                dp[0][j-1]
            )

        for i in range(1, n):
            dp[i][0] = max(
                num1[i] * num2[0],
                dp[i-1][0]
            )

        for i in range(1, n):
            for j in range(1, m):
                mul = num1[i] * num2[j]
                dp[i][j] = max(
                    mul,
                    mul + dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )

        return dp[-1][-1]
