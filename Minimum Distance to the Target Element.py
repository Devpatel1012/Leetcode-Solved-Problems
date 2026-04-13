class Solution(object):
    def getMinDistance(self, nums, target, start):
        ans = float("inf")

        for i,n in enumerate(nums):
            if n == target:
                ans = min(ans, abs(start - i))
        return ans
        