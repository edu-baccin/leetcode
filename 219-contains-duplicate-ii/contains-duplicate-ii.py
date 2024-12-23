class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        storage = {}

        for index, num in enumerate(nums):
            if num in storage:
                if index - storage[num] <=k:
                    return True
            
            storage[num] = index
        
        return False
