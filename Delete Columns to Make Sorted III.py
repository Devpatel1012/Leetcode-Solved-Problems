class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs[0])
        m = len(strs)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                check = True
                for r in range(m):
                    if strs[r][j]>strs[r][i]:
                        check = False
                        break
                if check:
                    dp[i] = max(dp[i],dp[j]+1)
        
        m = 0
        for i in dp:
            m = max(i,m)

        return n-m


