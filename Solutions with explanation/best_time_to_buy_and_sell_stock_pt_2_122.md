# Best Time to Buy and Sell Stock II

## Problem
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The core idea is to maximize profit by selling the stock whenever its price increases compared to the previous day. This strategy ensures that we capture all upward price movements. 

## Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize `total_profit` to 0.
2. Iterate through the array of stock prices.
3. For each day, compare the current day's price to the previous day's price.
4. If the current day's price is higher than the previous day's price, add the difference to total_profit.
5. By summing up all positive differences, we accumulate the maximum possible profit.

## Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Performance Metrics
- Runtime: Beats 55.05% of users with Python
- Memory: Beats 95.37% of users with Python

## Code
```
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
```