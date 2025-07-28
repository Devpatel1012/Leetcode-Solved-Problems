class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k %= n  # handle cases where k > len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse entire array
        reverse(0, n - 1)
        # Reverse first k elements
        reverse(0, k - 1)
        # Reverse remaining elements
        reverse(k, n - 1)


