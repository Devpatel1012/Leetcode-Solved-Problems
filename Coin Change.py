class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # turn = 0
        # if amount <= 0:
        #     return 0
        # else:
        #     coins = sorted(coins)
        #     n = len(coins)
        #     while amount>0:
        #         if coins[-1]<amount:
        #             n-=1
        #         elif amount<min(coins):
        #             return -1
        #         else:
        #             amount-=coins[-1]
        #             turn+=1
        #     return turn
        dp = [amount+1]*(amount+1)
        dp[0] = 0 
        for a in range(1,amount+1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(dp[a],1+dp[a-coin])
        return dp[amount] if dp[amount] != amount + 1 else -1