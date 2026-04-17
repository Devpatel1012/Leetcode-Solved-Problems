class Solution(object):
    def minMirrorPairDistance(self, nums):
        prev = dict()
        ans = float("inf")
        for i,val in enumerate(nums):
            if val in prev:
                ans = min(ans, abs(i-prev[val]))
            prev[int(str(val)[::-1])] = i
        return -1 if ans == float("inf") else ans
        