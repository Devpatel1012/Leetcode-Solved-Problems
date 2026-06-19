class Solution(object):
    def largestAltitude(self, gain):
        ans = 0
        prefixSum = 0
        for i in gain:
            prefixSum += i
            ans = max(ans,prefixSum)
        return ans
        