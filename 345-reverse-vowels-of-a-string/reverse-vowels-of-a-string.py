class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)

        count = 0
        dict_store = {}

        for letter in s:
            if letter in vowels:
                dict_store[count] = letter
            count += 1

        keys = list(dict_store.keys())

        for i in range(len(keys) // 2):
            dict_store[keys[i]], dict_store[keys[-1 - i]] = (
                dict_store[keys[-1 - i]],
                dict_store[keys[i]],
            )

        for key in keys:
            s[key] = dict_store[key]

        return "".join(s)
