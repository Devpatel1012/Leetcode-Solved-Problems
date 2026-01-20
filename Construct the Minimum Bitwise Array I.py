class Solution(object):
    def minBitwiseArray(self, nums):

        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            for i in range(1,32):
                if not (p&(1<<i)):
                    res = p^(1<<(i-1))
                    ans.append(res)
                    break
        return ans
