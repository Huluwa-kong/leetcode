class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = {e: i for i, e in enumerate(nums)}
        for i, e in enumerate(nums):
            d = target - e
            if d in num2idx and num2idx[d] != i:
                return i, num2idx[d]
