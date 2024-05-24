class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i, val in enumerate(prices[1:]):
            if val > prices[i]:
                total_profit += val - prices[i]

        return total_profit