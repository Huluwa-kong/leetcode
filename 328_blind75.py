from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left = []
        right = []
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
                right.append(1)
                continue
            left.append(left[i - 1] * nums[i - 1])
            j = -i
            # right[i - 1]
            right.append(nums[j] * right[i - 1])
        return [left[i] * right[-i - 1] for i in range(len(nums))]


print(Solution().productExceptSelf([1, 2, 3, 4]))
