class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        if target not  in nums:
            return result

        else:
            targetOfIndex = nums.index(target)
            result[0] = targetOfIndex
            for i in range(targetOfIndex,len(nums)):
                if (nums[i] == target):
                    result[1] = i
        return result