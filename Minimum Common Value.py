class Solution(object):
    def getCommon(self, nums1, nums2):
        ans = -1

        arr1Len = len(nums1)
        arr2Len = len(nums2)

        biggestLen = max(arr1Len, arr2Len)

        p1 = 0 
        p2 = 0

        while p1 < arr1Len and p2 < arr2Len:
            if p1 >= arr1Len:
                break

            if p2 >= arr2Len:
                break

            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] == nums2[p2]:
                ans = nums1[p1]
                break
            elif nums2[p2] > nums1[p1]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1
                

        return ans
        