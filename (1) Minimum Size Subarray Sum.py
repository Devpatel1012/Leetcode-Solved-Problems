# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         size = float('inf')
#         for i in range(len(nums)):
#             addition = nums[i]
#             if addition >= target:   # check single element case
#                 return 1
#             for j in range(i+1, len(nums)):
#                 addition += nums[j]
#                 if addition >= target:
#                     size = min(size, j - i + 1)
#                     break
#         return 0 if size == float('inf') else size
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:  # shrink window from left
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
