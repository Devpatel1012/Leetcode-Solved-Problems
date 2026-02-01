class Solution(object):
    def minimumCost(self, nums):
        ans = nums[0]
        cur, prev = float('inf'),float('inf')
        for i in range(1,len(nums)):
            if nums[i] < cur:
                if prev>cur:
                    prev = cur
                cur = nums[i]
            elif nums[i]< prev:
                prev = nums[i]
        ans += (cur+prev)
        return ans
