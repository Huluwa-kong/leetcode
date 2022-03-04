from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        for i in range(1, len(nums)):
            m = 1
            for j in range(i):
                k = 1 if nums[i] <= nums[j] else dp[j] + 1
                m = max(k, m)
            dp.append(m)
        return max(dp)


print(Solution().lengthOfLIS([1, 1, 1, ]))
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
