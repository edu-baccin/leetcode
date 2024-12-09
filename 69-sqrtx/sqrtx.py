class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start <= end:
            mid = (start + end) // 2
            squared = mid * mid

            if squared == x:
                return mid
            elif squared > x:
                end = mid - 1
            else:
                start = mid + 1

        return end
