class Solution:
    def maxOperations(self, nums):
        ans = 0
        ones = 0

        for i, c in enumerate(nums):
            if c == '1':
                ones += 1
            elif i + 1 == len(nums) or nums[i + 1] == '1':
                ans += ones

        return ans