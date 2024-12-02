class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)

        return [(candy + extraCandies) >= maxCandies for candy in candies]
