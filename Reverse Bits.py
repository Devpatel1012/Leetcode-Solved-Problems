class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
    

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = '{:032b}'.format(n)  
        print(binary)
        binaryrev = binary[::-1]
        print(binaryrev)
        return int(binaryrev,2)
        