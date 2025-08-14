class Solution:
    def numTrees(self, n):
        # dp[i] will store number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1  # empty tree
        dp[1] = 1  # single node

        # Fill the dp table
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1       # number of nodes in left subtree
                right = nodes - root  # number of nodes in right subtree
                total += dp[left] * dp[right]
            dp[nodes] = total

        return dp[n]
