class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = reversed(x)
        y = "".join(y)

        return x == y