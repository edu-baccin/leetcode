class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)

        return ''.join(result).lower() == ''.join(result[::-1]).lower()