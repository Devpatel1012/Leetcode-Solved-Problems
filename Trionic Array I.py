class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1. strictly increasing
        while i+1 < n and nums[i+1] > nums[i]:
            i += 1
        if i == 0:
            return False

        # 2. strictly decreasing
        j = i
        while j+1 < n and nums[j+1] < nums[j]:
            j += 1
        if j == i:
            return False

        # 3. strictly increasing
        k = j
        while k+1 < n and nums[k+1] > nums[k]:
            k += 1
        if k == j:
            return False

        return k == n-1