class Solution(object):
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        m = nums[0]
        prefixGCD = list()
        for i in nums:
            if i>m:
                m = i
            prefixGCD.append(gcd(i,m))
        prefixGCD.sort()
        s = 0
        j = -1
        for i in range(len(prefixGCD)//2):

            s+=gcd(prefixGCD[i],prefixGCD[j])
            j-=1
        return s

        