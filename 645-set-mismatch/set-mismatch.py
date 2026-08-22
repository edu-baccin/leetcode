class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        duplicate = 0
        for idx, num in enumerate(nums):
            if num == nums[idx-1]:
                duplicate = num
        missing = n * (1 + n) // 2 - (sum(nums) - duplicate)
        return [duplicate, missing]