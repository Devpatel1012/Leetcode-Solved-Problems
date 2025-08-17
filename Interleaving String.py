class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # def helper(i, j, k):
        #         # if we've matched all chars
        #         if k == len(s3):
        #             return i == len(s1) and j == len(s2)

        #         # greedy pick from s1
        #         if i < len(s1) and s1[i] == s3[k]:
        #             if helper(i+1, j, k+1):
        #                 return True

        #         # greedy pick from s2
        #         if j < len(s2) and s2[j] == s3[k]:
        #             if helper(i, j+1, k+1):
        #                 return True

        #         return False

        #     # quick check
        # if len(s1) + len(s2) != len(s3):
        #         return False

        # return helper(0, 0, 0)
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[len(s1)][len(s2)]
