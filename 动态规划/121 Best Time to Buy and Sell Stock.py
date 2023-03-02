from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 暴力O(n^2)超时
        return max([max(prices[i:]) - prices[i] for i in range(len(prices))])

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        F = [0] * len(prices)
        for i in range(1, len(prices)):
            F[i] = max(F[i - 1] + (prices[i] - prices[i - 1]), 0)
        return max(F)


price = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(price))
