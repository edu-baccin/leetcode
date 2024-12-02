from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        match = {")": "(", "]": "[", "}": "{"}
        stack = deque()

        for bracket in s:
            if bracket in match.values():
                stack.append(bracket)
            elif bracket in match.keys():
                if not stack or match[bracket] != stack.pop():
                    return False
                
        return not stack
