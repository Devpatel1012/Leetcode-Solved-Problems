class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = 0
        j = 0

        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1

            ans = max(ans, j - i)

        return n - ans



        