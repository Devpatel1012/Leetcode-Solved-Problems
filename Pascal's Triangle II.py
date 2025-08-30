class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """        
        my_list = [[0]*i for i in range(1, rowIndex+2)]
        
        for i in range(len(my_list)):
            n = len(my_list[i])
            for j in range(n):
                if j == 0 or j == n-1:
                    my_list[i][j] = 1
                else:
                    my_list[i][j] = my_list[i-1][j-1]+my_list[i-1][j]

        return my_list[rowIndex]
        