class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # dp[i][j] = number of subsequences of s[i:] that form t[j:]
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Base case: t is empty → 1 subsequence (empty string)
        for i in range(m+1):
            dp[i][n] = 1
        
        # Fill dp bottom-up
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]

# class Solution(object):
#     def numDistinct(self, s, t):
#         cache = {}
#         def dfs(i, j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0
#             if (i, j) in cache:
#                 return cache[(i, j)]
#             if s[i] == t[j]:
#                 cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
#             else:
#                 cache[(i, j)] = dfs(i+1, j)
#             return cache[(i, j)]
        # return dfs(0, 0)
