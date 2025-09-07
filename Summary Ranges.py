class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        res = []
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:  # break in sequence
                if prev != nums[i-1]:
                    res.append(str(prev) + "->" + str(nums[i-1]))
                else:
                    res.append(str(prev))
                prev = nums[i]

        # Add the last range
        if prev != nums[-1]:
            res.append(str(prev) + "->" + str(nums[-1]))
        else:
            res.append(str(prev))

        return res