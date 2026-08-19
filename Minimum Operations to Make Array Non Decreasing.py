class Solution(object):
    def minOperations(self, nums):
        curr = nums[0]
        ratio = 0
        for i in range(1,len(nums)):
            nums[i] += ratio
            if nums[i]>=curr :
                curr = nums[i]
                continue
            diff = curr - nums[i]
            ratio+=diff
            nums[i] += diff
            curr = nums[i]
        return ratio
        


        