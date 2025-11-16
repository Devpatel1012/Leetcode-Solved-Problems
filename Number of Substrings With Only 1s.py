class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9 + 7

        count = 0
        ans = 0
         
        for n in nums:
            if n=='1':
                count += 1
            else:
                ans += ((count*(count+1))//2)%mod
                count =0

        ans += ((count*(count+1))//2)%mod
        
        return ans 