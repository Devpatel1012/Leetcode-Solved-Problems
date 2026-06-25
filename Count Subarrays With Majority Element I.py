class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        ans = 0
        n = len(nums)
        for i in range(n):
            tar = 0
            for j in range(i,n):
                if nums[j] == target:
                    tar+=1
                length = j-i+1
                if tar > length//2:
                    ans+=1
        return ans

        