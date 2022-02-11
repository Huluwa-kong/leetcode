from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = None
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                v = min(height[i], height[j]) * (j - i)
                if m is None or m < v:
                    m = v
        return m
