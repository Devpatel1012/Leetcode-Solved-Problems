class Solution(object):
    def findGCD(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        mi = min(nums)
        ma = max(nums)
        return gcd(mi,ma)
        