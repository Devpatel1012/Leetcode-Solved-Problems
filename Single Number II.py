class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for item in nums:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        for key, value in counts.items():
            if value == 1:
                return key