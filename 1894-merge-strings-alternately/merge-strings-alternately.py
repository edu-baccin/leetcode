class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0

        merged_string = []

        while i < len(word1) + len(word2):
            if i < len(word1):
                merged_string.append(word1[i])
            if i < len(word2):
                merged_string.append(word2[i])
            i += 1

        return "".join(merged_string)
