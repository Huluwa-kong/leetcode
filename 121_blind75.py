from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        cur_min = prices[0]
        best = None
        for i, e in enumerate(prices):
            if i == 0:
                continue
            if e > cur_min and (best is None or e - cur_min > best):
                best = e - cur_min

            cur_min = min(e, cur_min)
        return best or 0


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
