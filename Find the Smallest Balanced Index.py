class Solution(object):
    def smallestBalancedIndex(self, nums):
        s = sum(nums) - nums[-1]
        prod = 1 

        i = len(nums) - 1
        while prod < s: 
            i -= 1
            s -= nums[i]
            prod *= nums[i+1]
        return i if prod == s else -1