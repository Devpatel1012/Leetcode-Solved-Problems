class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums) % p
        if total == 0:
            return 0
        
        prefix = 0
        idx_map = {0: -1}
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - total) % p # till now does not about the -number and modulo property 
            if target in idx_map:
                min_len = min(min_len, i - idx_map[target])
            idx_map[prefix] = i
        
        return min_len if min_len < len(nums) else -1