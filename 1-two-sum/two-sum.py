class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            y = target - x

            if y in nums[i+1:]:
                return i, nums[i+1:].index(y) + (i + 1)
