# class Solution:
#     def maxProfit(self, prices) -> int:
#         # TC -> N, SC -> N
#         buy = min(prices)
#         for i in range(len(prices)):
#             if prices[i] == buy:
#                 new_prices = prices[i:]
#         sale = max(new_prices)
#         return sale - buy
#
# class Solution:
#     # TC -> N, SC -> 1
#     def maxProfit(self, prices) -> int:
#         buy,sell = 0,1
#         maxP = 0
#         while sell < len(prices):
#             if prices[buy] < prices[sell]:
#                 profit = prices[sell] - prices[buy]
#                 maxP = max(maxP, profit)
#             else:
#                 buy = sell
#             sell += 1
#         return maxP

class Solution:
    def maxProfit(self, prices) -> int:
        minBuy = prices[0]
        maxP = 0
        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

if __name__ == "__main__":
    prices = [4,3,6,5,10]
    sol = Solution()
    print(sol.maxProfit(prices))