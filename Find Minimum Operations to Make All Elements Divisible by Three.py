class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            if i%3 != 0:
                ans+=1
        return ans