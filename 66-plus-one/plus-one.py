class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        counter = len(digits) - 1
        result = 0

        for digit in digits:
            result += digit * (10 ** counter)
            counter -= 1

        result = result + 1
        result = map(int,str(result))
        result = list(result)
        
        return result