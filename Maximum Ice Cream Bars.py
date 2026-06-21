class Solution(object):
    def maxIceCream(self, costs, coins):
        if coins<min(costs):
            return 0

        costs.sort()
        ans = 0
        s = sum(costs)
        for i in range(len(costs)):
            if coins and ((coins-costs[i]) >= 0):
                coins-=costs[i]
                ans+=1
        return ans

        