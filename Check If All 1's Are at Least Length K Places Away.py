class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

       
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 1:
                if 1 in nums[i+1:i+k+1]:
                    return False
                i = i+k+1 
            else:
                i+=1
        return True