class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # from collections import defaultdict

        # # Step 1: Count occurrences
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        # # Step 2: Build the result with at most two duplicates
        # result = []
        # for num in sorted(count.keys()):
        #     occurrences = min(2, count[num])
        #     result.extend([num] * occurrences)

        # # Step 3: Modify the original nums in-place
        # for i in range(len(result)):
        #     nums[i] = result[i]

        # # Step 4: Trim the rest (if needed)
        # return len(result)
        
        if len(nums) <= 2:
            return len(nums)
        
        write_index = 2  # Start from index 2 because first 2 elements are always valid

        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
