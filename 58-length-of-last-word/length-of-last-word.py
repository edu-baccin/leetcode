class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()

        return len(strs[-1])
