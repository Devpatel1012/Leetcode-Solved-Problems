class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
        
            return nums.index(target)
        except ValueError:
          
            if not nums:
                return 0

            for i in range(len(nums)):
                if nums[i] > target: 
                    return i
                elif nums[i] == target:
                    return i
            return len(nums)