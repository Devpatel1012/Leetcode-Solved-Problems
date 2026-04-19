class Solution(object):
    def maxDistance(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        dist=0
        i = 0
        j = 0
        while i<n and j<m:
            if nums1[i] <= nums2[j]:
                dist = max(dist, (j-i))
                j += 1
            else:
                i += 1
        return dist