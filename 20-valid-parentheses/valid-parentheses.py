from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        left_side = ["(", "[", "{"]
        right_side = [")", "]", "}"]
        match = ["()", "[]", "{}"]
        stack = deque()

        for bracket in s:
            if bracket in left_side:
                stack.append(bracket)
            elif len(stack) > 0 and stack[-1] + bracket in match:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
