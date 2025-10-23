class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def make_pairs(nums):
            return [[nums[i], nums[i+1]] for i in range(len(nums)-1)]
        
        def mod_sum(pair):
            return (pair[0] + pair[1]) % 10

        nums = [int(ch) for ch in s]
        
        while len(nums) > 2:
            pairs = make_pairs(nums)
            nums = [mod_sum(p) for p in pairs]
        
        return nums[0] == nums[1]

        