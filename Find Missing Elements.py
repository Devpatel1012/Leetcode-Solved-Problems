class Solution(object):
    def findMissingElements(self, nums):
        mi,ma = min(nums),max(nums)
        full = list(range(mi,ma+1))
        ans = sorted(list(set(full) - (set(full)&set(nums))))
        return ans
        