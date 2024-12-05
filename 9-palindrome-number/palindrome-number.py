class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = reversed(x)
        y = "".join(y)

        if y == x:
            return True
        else:
            return False
