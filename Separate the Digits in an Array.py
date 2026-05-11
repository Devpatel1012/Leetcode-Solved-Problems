class Solution(object):
    def separateDigits(self, nums):
        ans = []
        for i in nums:
            ans.extend(map(int,str(i)))
        return ans
        