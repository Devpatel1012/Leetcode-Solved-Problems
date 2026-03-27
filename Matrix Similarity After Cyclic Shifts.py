class Solution(object):
    def areSimilar(self, mat, k):
        n, m = len(mat), len(mat[0])
        shift = k%m

        if shift == 0:
            return True
        
        for i,row in enumerate(mat):
            if i%2 == 0:
                shifted = row[shift:]+row[:shift]
            else:
                shifted = row[-shift:]+row[:-shift]
            if row != shifted:
                return False
        
        return True
        
