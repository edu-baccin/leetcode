class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        for x,y in enumerate(nums[:int(len(nums)/2)]):
            result.append(nums[x])
            result.append(nums[x+n])
        return result