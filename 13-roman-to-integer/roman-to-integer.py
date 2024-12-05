class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev_letter = ""

        for letter in s:
            result += roman[letter]
            if prev_letter == "I" and (letter == "V" or letter == "X"):
                result -= 2 * roman[prev_letter]
            if prev_letter == "X" and (letter == "L" or letter == "C"):
                result -= 2 * roman[prev_letter]
            if prev_letter == "C" and (letter == "D" or letter == "M"):
                result -= 2 * roman[prev_letter]

            prev_letter = letter

        return result
