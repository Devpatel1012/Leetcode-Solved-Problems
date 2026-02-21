class Solution(object):
    def countPrimeSetBits(self, left, right):
        p = {2,3,5,7,11,13,17,19,23,29}
        ans = 0
        for num in range(left, right + 1):
            if bin(num).count('1') in p:
                ans+=1
        return ans
        