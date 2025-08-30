# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices or len(prices) < 2:
#             return 0

#         total_profit = []
#         result = 0

#         # collect all positive differences
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 total_profit.append(prices[i] - prices[i-1])

#         # if there are fewer than 2 profitable trades
#         if len(total_profit) == 0:
#             return 0
#         if len(total_profit) == 1:
#             return total_profit[0]

#         print(total_profit)
#         # take two largest profits
#         totalmax = max(total_profit)
#         result += totalmax
#         total_profit.remove(totalmax)
#         totalmax = max(total_profit)
#         result += totalmax

#         return result
class Solution(object):
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)          # first buy
            sell1 = max(sell1, buy1 + price)  # first sell
            buy2 = max(buy2, sell1 - price)   # second buy
            sell2 = max(sell2, buy2 + price)  # second sell

        return sell2
