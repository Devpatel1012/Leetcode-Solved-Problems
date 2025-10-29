class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_str = bin(n)[2:]
        
        all_ones = '1' * len(binary_str)
        
        result = int(all_ones, 2)
        
        if result < n:
            result = int('1' * (len(binary_str) + 1), 2)
        
        return result