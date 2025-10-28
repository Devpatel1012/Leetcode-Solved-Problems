class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)   
        left_sum = 0            
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                right_sum = total_sum - left_sum
                
                if left_sum == right_sum:
                    ans += 2
                elif abs(left_sum - right_sum) == 1:
                    ans += 1
            else:
                left_sum += nums[i]

        return ans
        