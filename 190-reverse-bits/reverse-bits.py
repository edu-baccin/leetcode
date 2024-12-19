class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = format(n, '0{}b'.format(32))
        n = n[::-1]

        return int(n, 2)
        