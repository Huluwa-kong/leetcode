from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = dict()
        for i, e in enumerate(nums):
            if e not in indices:
                indices[e] = 0
            indices[e] += 1
        ans = set()
        for i, a in enumerate(nums):
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -(a + b)
                if c in indices:
                    num = indices[c]
                    if a == c:
                        num -= 1
                    if b == c:
                        num -= 1
                    if num:
                        r = tuple(sorted([a, b, c]))
                        ans.add(r)
        ans = [list(e) for e in ans]
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
