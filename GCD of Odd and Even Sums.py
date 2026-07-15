class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        odd,even =1,2
        sumodd,sumeven = 1,2
        for i in range(n-1):
            odd+=2
            even+=2
            sumodd += odd
            sumeven+=even
        return gcd(sumodd,sumeven)
        
        