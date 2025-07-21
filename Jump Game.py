class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current =0
        farthest = 0
        for i in range(len(nums)):
            farthest = max(farthest,i+nums[i])
            
            if i == current :
                current = farthest
        if current == (len(nums)-1) or current > (len(nums)-1) :
            return True
        else:
            return False