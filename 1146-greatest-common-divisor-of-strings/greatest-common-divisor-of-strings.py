class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)

        while b != 0:
            a, b = b, a % b
        
        result = str1[:a] # could be str2[:a] too

        if str1 == result * (len(str1) // a) and str2 == result * (len(str2) // a):
            return result
        else:
            return ''


            


            
