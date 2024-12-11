class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        unique = set(nums)

        for num in unique:
            if nums.count(num) > len(nums)/2:
                return num
