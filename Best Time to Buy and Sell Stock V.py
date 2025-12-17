class Solution(object):
    def maximumProfit(self, A, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        bought = [float('-inf')] * k
        res = [0] * (k + 1)
        sold = [0] * k
        for a in A:
            for j in range(k, 0, -1):
                res[j] = max(res[j], bought[j - 1] + a, sold[j - 1] - a)
                bought[j - 1] = max(bought[j - 1], res[j - 1] - a)
                sold[j - 1] = max(sold[j - 1], res[j - 1] + a)
                # print(j,a)
                # print(res,bought,sold)
        return max(res)