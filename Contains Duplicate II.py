class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # n = len(nums)
        # for i in range(n):
        #     # Check next k elements
        #     for j in range(i + 1, min(i + k + 1, n)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        seen = {}  # num -> last index

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i  # update last seen index
        return False