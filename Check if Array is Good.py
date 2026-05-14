class Solution(object):
    def isGood(self, nums):
        maxNum = max(nums)
        n = len(nums)
        if len(set(nums)) == maxNum:
            if n != maxNum+1:
                return False
            if nums.count(maxNum)==2:
                return True
        return False            


        