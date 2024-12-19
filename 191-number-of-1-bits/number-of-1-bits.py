class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = bin(n)[2:]
        a = list(str(a))
        a = a.count("1")

        return a
