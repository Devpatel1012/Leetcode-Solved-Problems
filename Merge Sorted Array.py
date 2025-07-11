class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start filling nums1 from the end
        i = m - 1  # Last element in nums1 (real part)
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last index in nums1 (full size)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        

        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
                
            


# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         count = m
#         for i in range(len(nums2)):
#             nums1[count] = nums2[i]
#             count = count+1
#         nums1.sort()
        
