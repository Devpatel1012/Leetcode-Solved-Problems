class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Pointer for the position of non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move valid element to the front
                k += 1

        return k