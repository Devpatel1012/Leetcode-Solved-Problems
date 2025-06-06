class Solution(object):
    def mergearray(self,num1,num2):
        num3 = num1 +num2
        num3.sort()
        return num3

    def findMedianSortedArrays(self, nums1, nums2):
        ans = 0
        ansarray = self.mergearray(nums1,nums2)
        leng = len(ansarray)
        if ((leng % 2) == 0):
            med1 = (leng)//2 
            med2 = med1 - 1
            ans = (ansarray[med1] + ansarray[med2]) / 2.0  
        else:
            med = (((leng)//2))
            ans = ansarray[med]
        return ans

solu = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(solu.findMedianSortedArrays(nums1,nums2))