class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            result = 0

            while n > 0:
                digit = n % 10
                result += digit ** 2
                n = n // 10
            
            n = result
        
        return n == 1
