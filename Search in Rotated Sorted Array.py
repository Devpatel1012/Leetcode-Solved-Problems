class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            middle = (low + high) // 2
            
            # Case 1: Target found at the middle
            if nums[middle] == target:
                return middle
            
            # Case 2: Determine if the left half is sorted (nums[low] to nums[middle])
            # This is true if nums[low] <= nums[middle]
            if nums[low] <= nums[middle]:
                # If the left half is sorted, check if target falls within its range
                if nums[low] <= target < nums[middle]:
                    # Target is in the sorted left half, so narrow search to left
                    high = middle - 1
                else:
                    # Target is NOT in the sorted left half, so it must be in the unsorted right half
                    low = middle + 1
            
            # Case 3: The left half is NOT sorted, which means the right half MUST be sorted
            # This happens if nums[low] > nums[middle] (the pivot is in the left half)
            else: # nums[middle] < nums[low]
                # If the right half is sorted, check if target falls within its range
                if nums[middle] < target <= nums[high]:
                    # Target is in the sorted right half, so narrow search to right
                    low = middle + 1
                else:
                    # Target is NOT in the sorted right half, so it must be in the unsorted left half
                    high = middle - 1
                    
        # If the loop finishes, the target was not found
        return -1