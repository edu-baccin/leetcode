class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srt = sorted(nums, reverse=True)
        result=[]
        for num in nums:
            result.append(srt[::-1].index(num))
        return result