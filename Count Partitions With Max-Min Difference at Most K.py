class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [1] + [0]*n
        mod = 10**9 +7
        acc = 1
        sl = SortedList()

        l = 0
        for i in range(n):
            sl.add(nums[i])
            while sl[-1]-sl[0]>k :
                sl.remove(nums[l])
                acc = (acc-dp[l])%mod
                l+=1
            dp[i+1] = acc
            acc = (dp[i+1]+acc)%mod
        return dp[-1]