class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i]:
                result[i] = nums[(i + nums[i]) % n]

        return result