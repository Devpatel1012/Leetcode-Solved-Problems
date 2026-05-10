class Solution(object):
    def maximumJumps(self, nums, target):
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return 0

            res = float('-inf')

            for j in xrange(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dfs(j) + 1)

            memo[i] = res
            return res

        ans = dfs(0)

        return -1 if ans < 0 else ans