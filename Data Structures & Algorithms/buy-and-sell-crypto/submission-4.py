class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                right += 1
            elif profit >= 0:
                max_profit = max(max_profit, profit)
                right += 1
        right -= 1
        while left < right:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            left += 1

        return max_profit
