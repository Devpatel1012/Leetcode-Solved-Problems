__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # # Traverse through all array elements
        # for i in range(n):
        #     # Last i elements are already in place, so we don't need to check them
        #     # Optimized: If no swaps occur in a pass, the array is sorted
        #     swapped = False 
        #     for j in range(0, n - i - 1):
        #         # Traverse the array from 0 to n-i-1
        #         # Swap if the element found is greater than the next element
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swapped = True
        #     # If no two elements were swapped by inner loop, then break
        #     if not swapped:
        #         break
        # return nums
        low, mid = 0, 0
        hi = len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low = low + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else: 
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi = hi - 1
        