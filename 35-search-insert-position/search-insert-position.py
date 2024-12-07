class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            if i == len(nums) - 1 and target > nums[-1]:
                return i + 1
