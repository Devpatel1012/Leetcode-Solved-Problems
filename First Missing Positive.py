class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if 1 not in nums:
            return 1

        # Filter only positive numbers and create a set for fast lookup
        positive_set = set(num for num in nums if num > 0)

        # Try from 1 to len(nums) + 1 to find the first missing positive
        for i in range(1, len(nums) + 2):
            if i not in positive_set:
                return i

# class Solution(object):
#     def firstMissingPositive(self, nums):
#         s=set(nums)
#         for x in xrange(1, len(nums)+2):
#             if x not in s:
#                 return x
            
#         #  only for pyhton2 version not workable in python3
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
