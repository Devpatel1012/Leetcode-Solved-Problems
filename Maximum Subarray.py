from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
     
        if not nums:
            return 0 

        global_max = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            
            current_max = max(num, current_max + num)

        
            global_max = max(global_max, current_max)

        return global_max