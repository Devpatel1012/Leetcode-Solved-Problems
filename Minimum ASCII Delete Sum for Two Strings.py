class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s1)
        m = len(s2)

        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+(ord(s1[i-1]))
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        a = (dp[-1][-1])

        o1 = sum([ord(s) for s in s1])

        o2 = sum([ord(s) for s in s2])
        ans = (o1-a) + (o2-a)
        return ans

        

