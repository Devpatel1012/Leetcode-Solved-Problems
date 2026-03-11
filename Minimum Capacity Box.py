class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        
        capa = float('inf')
        indx = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capa > capacity[i]:
                capa = capacity[i]
                indx = i
        return indx


        