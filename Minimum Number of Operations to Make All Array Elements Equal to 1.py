from fractions import gcd
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        ones = nums.count(1)
        if ones:
            return n-ones

        g = nums[0]
        for num in nums:
            g = gcd(g,num)
        if g > 1:
            return -1

        min_len = float('inf')
        for i in range(n):
                g = nums[i]
                for j in range(i,n):
                    g = gcd(g,nums[j])
                    if g == 1:
                        min_len = min(min_len,j-i+1)
                        break

        return (min_len-1) + (n-1)


        
        