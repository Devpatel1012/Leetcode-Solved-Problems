class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """


        # TLE
        ans = sum(x * y for x, y in zip(prices, strategy))
        n = len(prices)
      
        new =[0]*(k//2)+[1]*(k//2)
        for i in range(n-k+1):
            s = strategy[:]             
            s[i : i+k] = new
            current_sum = sum(x * y for x, y in zip(prices, s))
            ans = max(ans, current_sum)
            
        return ans

        # Without TLE
        
class Solution(object):
            def maxProfit(self, p, s, k):
                """
                :type prices: List[int]
                :type strategy: List[int]
                :type k: int
                :rtype: int
                """

                n = len(p)
                base = [p[i]*s[i] for i in range(n)]
                bs = sum(base)

                bp = [0]*(n+1)
                for i in range(n):
                    bp[i+1] = bp[i]+base[i]        

                pp = [0]*(n+1)
                for i in range(n):
                    pp[i+1] = pp[i]+p[i]

                ans = bs
                h = k//2
                for i in range(n-k+1):
                    old = bp[i+k] - bp[i]
                    new = pp[i+k] - pp[i+h]
                    s = bs - old+new
                    ans = max(ans,s)
                return ans

                        