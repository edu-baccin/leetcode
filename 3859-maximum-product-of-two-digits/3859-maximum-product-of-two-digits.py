class Solution:
    def maxProduct(self, n: int) -> int:
        digit_list = [int(d) for d in str(n)]
        digit_list.sort(reverse=True)
        result = None

        if digit_list and len(digit_list) > 1:
            result = digit_list[0] * digit_list[1]
        return result
