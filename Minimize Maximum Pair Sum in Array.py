class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        nums.sort()
        n = len(nums)
        lp = n-1
        for i in range(n//2):
            cur = nums[i]+nums[lp]
            lp -= 1
            sums.append(cur)
        return max(sums)

