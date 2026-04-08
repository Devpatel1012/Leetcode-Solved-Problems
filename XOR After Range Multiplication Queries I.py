class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = (10**9 +7)
        for l,r,k,v in queries:
            for j in range(l,r+1,k):
                nums[j] = (nums[j]*v)%MOD
        ans = 0
        for i in nums:
            ans^=i
        return ans
            

        