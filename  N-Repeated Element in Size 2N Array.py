from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for i,j in c.items():
            if j>1:
                return i

        # 
        l=len(nums)/2
        for i in nums:
            if nums.count(i)==l:
                return i
        
